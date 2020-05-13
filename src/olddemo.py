import sys
import fire
import json
import os
import numpy as np
import tensorflow as tf
import model, sample, encoder

import generate_unconditional_samples

import interactive_conditional_samples

class GPT2: 
  # extracted from the source code to generate some text based on a prior
  def __init__(
      self,
      models_dir='models',
      model_name='1558M',
      seed=None,
      nsamples=1,
      batch_size=1,
      length=None,
      temperature=1,
      top_k=0,
      raw_text="",
  ):
      """
      Interactively run the model
      :model_name=1558M : String, which model to use
      :seed=None : Integer seed for random number generators, fix seed to reproduce
       results
      :nsamples=1 : Number of samples to return total
      :batch_size=1 : Number of batches (only affects speed/memory).  Must divide nsamples.
      :length=None : Number of tokens in generated text, if None (default), is
       determined by model hyperparameters
      :temperature=1 : Float value controlling randomness in boltzmann
       distribution. Lower temperature results in less random completions. As the
       temperature approaches zero, the model will become deterministic and
       repetitive. Higher temperature results in more random completions.
      :top_k=0 : Integer value controlling diversity. 1 means only 1 word is
       considered for each step (token), resulting in deterministic completions,
       while 40 means 40 words are considered at each step. 0 (default) is a
       special setting meaning no restrictions. 40 generally is a good value.
      """
      if batch_size is None:
          batch_size = 1
      assert nsamples % batch_size == 0

      self.nsamples = nsamples
      self.batch_size = batch_size
      models_dir = os.path.expanduser(os.path.expandvars(models_dir))
      self.enc = encoder.get_encoder(model_name, models_dir = 'models')
      hparams = model.default_hparams()
      with open(os.path.join(models_dir, model_name, 'hparams.json')) as f:
          hparams.override_from_dict(json.load(f))

      if length is None:
          length = hparams.n_ctx // 2
      elif length > hparams.n_ctx:
          raise ValueError("Can't get samples longer than window size: %s" % hparams.n_ctx)

      self.sess = tf.Session(graph=tf.Graph())
      self.sess.__enter__()
      
      self.context = tf.placeholder(tf.int32, [batch_size, None])
      np.random.seed(seed)
      tf.set_random_seed(seed)
      self.output = sample.sample_sequence(
          hparams=hparams, length=length,
          context=self.context,
          batch_size=batch_size,
          temperature=temperature, top_k=top_k
      )

      saver = tf.train.Saver()
      self.ckpt = tf.train.latest_checkpoint(os.path.join('models', model_name))
      saver.restore(self.sess, self.ckpt)

  def close(self):
    self.sess.close()
  
  def generate_conditional(self,raw_text):
      context_tokens = self.enc.encode(raw_text)
      generated = 0
      for _ in range(self.nsamples // self.batch_size):
          out = self.sess.run(self.output, feed_dict={
              self.context: [context_tokens for _ in range(self.batch_size)]
          })[:, len(context_tokens):]
          for i in range(self.batch_size):
              generated += 1
              text = self.enc.decode(out[i])
              return text
              #print("=" * 40 + " SAMPLE " + str(generated) + " " + "=" * 40)
              #print(text)
      #print("=" * 80)
###  
	  
gpt2 = GPT2(model_name="1558M")
###
class Who:
  """A class defining the conversation parties: me, he"""
  def __init__(self):
    self.prefixes = []

  def matches(self,phrase):
    for prefix in self.prefixes:
      if phrase.startswith(prefix):
        #print(f"{phrase} starts with {prefix}")
        return True
      
    #print(f"{phrase} does not start with {self.prefixes}")
    return False

  def get_random_prefix(self):
    return self.prefixes[0]
  
class Me(Who):
  def __init__(self):
    super().__init__()
    self.prefixes = ["I said: \""]
   
  
class You(Who):
  def __init__(self):
    super().__init__()
    self.prefixes = ["You said: \""]

class Conversation:
  
  def __init__(self, prior = None):
    if prior is None:
      prior="""
      You said: "Nice to meet you. What's your name?"
      I said: "My name is Pete."
      You said: "That's an interesting name. How old are you?"
      I said: "I'm 40 years old."
      You said: "Can you tell me something about yourself?"
      I said: "Ofcourse! I like playing video games and eating cake. "
      You said: "I like sweet stuff too. What are your plans for tomorrow?"
      """
    self.suggestion = None
    
    self.me = Me()
    self.you = You()
    self.parties  = [ self.me, self.you ]
    
    self.conversation = []
    
    lines = prior.split("\n")
    for line in lines:
      line = line.strip()
      if len(line)!=0:
        party = None
        for party in self.parties:
          if party.matches(line):
            break
        if party is None:
          raise Exception(f"Unknown party: {line}")
                
        self.conversation.append((party,line))
    self.get_suggestion()
    
  
  def get_prior(self):
    conv = ""
    for (party, line) in self.conversation:
      conv+=line+"\n"
    return conv
  
  def get_suggestion(self):
    who, last_line = self.conversation[-1]

    party_index = self.parties.index(who)
    next_party = self.parties[(party_index+1) % len(self.parties)]
      
    conv = self.get_prior()
    conv += next_party.get_random_prefix()
    answer = self.get_answer(next_party, conv)

    if not next_party.matches(answer):
      prefix = next_party.get_random_prefix()
      answer = prefix + answer
    
    self.suggestion = (next_party, answer)
  
  def next(self, party = None, answer = ""):
    """Continue the conversation
    :param party: None -> use the current party which is currently in turn
    :param answer: None -> use the suggestion, specify a text to override the 
           suggestion
    
    """
    suggested_party, suggested_answer = self.suggestion
    if party is None:
      party = suggested_party
    
    if answer == "":
      answer = suggested_answer
      
    if not party.matches(answer):
      prefix = party.get_random_prefix()
      answer = prefix + answer
    
    answer = answer.strip()
    if answer[-1] != "\"":
      # add the closing "
      answer += "\""
      
    self.conversation.append((party, answer))    
    self.get_suggestion()
    
  def retry(self):
    self.get_suggestion()
        
  def get_answer(self, party, conv):
    answer = gpt2.generate_conditional(raw_text=conv)
    lines = answer.split("\n")
    line = ""
    for line in lines:
      if line !="":
        break
      
    if line!="":
      return line
    
    return ""
      
  def show(self):
    conv = ""
    for (party, line) in self.conversation:
      conv+=line+"\n"
    print(conv)
    if self.suggestion is not None:
      party, answer  = self.suggestion
      print("--> "+answer)
	  
	  
c = Conversation()
c.show()
c.retry()
c.show()
c.next()
c.show()
c.retry()
c.next(c.you, "Pizza is not to good for your health though.")
c.show()
gpt2.close()

# This is for possible future development but way slow out of date etc.
