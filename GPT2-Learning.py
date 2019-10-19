#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import fire, json, os, string, sys, threading
import model, sample, encoder, logging, time
import numpy as np
import tensorflow as tf
# This tests the encoding is not going to error.
print(sys.stdout.encoding)
print(u"Stöcker".encode(sys.stdout.encoding, errors='replace'))
print (u"Стоескер".encode(sys.stdout.encoding, errors='replace'))
# End of test.

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
mode = False
learn = False
learning = ""
user = ""
running = False
tim = 1800
lock_tim = threading.Lock()
translator = str.maketrans('', '', string.punctuation)
# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    global running
    global mode
    global learn
    if running == False:
        mode = False
        learn = False
        global learning
        learning = ""
    else:
        global tim
        left = str(tim)
        update.message.reply_text('Bot is currently in use, make sure to set your settings when their timer runs down. ' + left + ' seconds.')
    if mode == True and learn == True:
        update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: 0.75 Rate:1 GPT-2 774M. I am in the learning chatbot mode.')
    if mode == True and learn == False:
        update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: 0.75 Rate:1 GPT-2 774M I am in the chatbot mode.')
    if mode == False:
        update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: 0.75 Rate:1 GPT-2 774M I am in the finishsentence mode.')
def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Just type a message... It could be lagged out. /chatbot goes into Me: You: mode. /finish just finishes the text /learnon for conversation learning mode.')
def chatbot(bot, update):
    """Send a message when the command /chatbot is issued."""
    global running
    global mode
    global learn
    if running == False:
        mode = True
        learn = False
        global learning
        learning = ""
    else:
        global tim
        left = str(tim)
        update.message.reply_text('Bot is currently in use, make sure to set your settings when their timer runs down. ' + left + ' seconds.')
    update.message.reply_text('Just type a message... It could be lagged out. This is the Chatbot mode, it adds Me: and You: to the input text.')
def finish(bot, update):
    """Send a message when the command /finish is issued."""
    global running
    global mode
    global learn
    if running == False:
        mode = False
        learn = False
        global learning
        learning = ""
    else:
        global tim
        left = str(tim)
        update.message.reply_text('Bot is currently in use, make sure to set your settings when their timer runs down. ' + left + ' seconds.')
    update.message.reply_text('Just type a message... It could be lagged out. This is the Finish Sentence mode, the default strings apply.')
def learnon(bot, update):
    """Send a message when the command /finish is issued."""
    global running
    global mode
    global learn
    if running == False:
        mode = True
        learn = True
        global learning
        learning = ""
    else:
        global tim
        left = str(tim)
        update.message.reply_text('Bot is currently in use, make sure to set your settings when their timer runs down. ' + left + ' seconds.')
    update.message.reply_text('Just type a message... It could be lagged out. This is the Chatbot mode, it adds Me: and You: to the input text with learning. Use /learnreset to reset the conversation.')
def learnoff(bot, update):
    """Send a message when the command /finish is issued."""
    global running
    global mode
    global learn
    if running == False:
        mode = True
        learn = False
        global learning
        learning = ""
    else:
        global tim
        left = str(tim)
        update.message.reply_text('Bot is currently in use, make sure to set your settings when their timer runs down. ' + left + ' seconds.')
    update.message.reply_text('Just type a message... It could be lagged out. This is the Chatbot mode. Learning mode has been turned off.')
def learnreset(bot, update):
    """Send a message when the command /finish is issued."""
    global running
    global mode
    global learn
    if running == False:
        mode = True
        learn = True
        global learning
        learning = ""
    else:
        global tim
        left = str(tim)
        update.message.reply_text('Bot is currently in use, make sure to set your settings when their timer runs down. ' + left + ' seconds.')
    update.message.reply_text('Just type a message... It could be lagged out. Learning mode has been reset.')

def regex(mew):
    meow = mew
    if "Me:" in meow:
        meow = meow.rsplit('Me:')[0]
        return meow
    if "You:" in meow:
        meow = meow.rsplit('You:')[0]
        return meow
    if "?" in meow:
        meow = meow.rsplit('?', 1)[0]
        meow = meow + "?"
        return meow
    if "!" in meow:
        meow = meow.rsplit('!', 1)[0]
        meow = meow + "!"
        return meow
    else:
        meow = meow.rsplit('.', 1)[0]
        meow = meow + "."
        return meow
    return meow


def runn(bot, update):
    comput = threading.Thread(target=wait, args=(bot, update,))
    comput.start()
def wait(bot, update):
    global tim
    global user
    global running
    if user == "":
        user = update.message.from_user.id
    if user == update.message.from_user.id:
        user = update.message.from_user.id
        lock_tim.acquire()
        tim = 1800
        lock_tim.release()
        running = True
        compute = threading.Thread(target=interact_model, args=(bot, update,))
        compute.start()
        while tim > 1:
            time.sleep(1)
            lock_tim.acquire()
            tim = tim - 1
            lock_tim.release()
            # print(tim) THIS IS FOR DEBUG
        global mode
        global learn
        mode = False
        learn = False
        global learning
        learning = ""
        if running == True:
            running = False
            user = ""
            update.message.reply_text('Timer has run down, bot has been reset into the default mode.')
        
    else:
        lock_tim.acquire()
        left = str(tim)
        lock_tim.release()
        update.message.reply_text('Bot is in use, current cooldown is: ' + left + ' seconds.')

def interact_model(bot, update):
    model_name = '774M'
    seed = None
    nsamples = 1
    batch_size = 1
    temperature = 1
    top_k = 0
    top_p = 0.75
    models_dir = 'models'
    tex = update.message.text
    penguin = str(tex)
    global learning
    global learn
    # This does some basic length processing. This way it can try and answer open-ended questions in chatbot mode.
    global mode
    if mode == True:
        cat = len(penguin.split(" "))
        if cat < 17:
            cat = 17
        if cat > 17:
            cat = cat / 17
            cat = round(cat) * 17
        length = cat
        wolf = "Me: " + penguin
        initial = wolf + " You:"
        raw_text = learning + initial
    if mode == False:
        cat = len(penguin.split(" "))
        if cat < 17:
            cat = 17
        if cat > 17:
            cat = cat / 17
            cat = round(cat) * 17
        length = cat
        raw_text = penguin
    if mode == True and learn == True:
        update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: 0.75 Rate:1 GPT-2 774M. I am in the learning chatbot mode. Computing...')
    if mode == True and learn == False:
        update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: 0.75 Rate:1 GPT-2 774M I am in the chatbot mode. Computing...')
    if mode == False:
        update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: 0.75 Rate:1 GPT-2 774M I am in the finishsentence mode. Computing...')
    models_dir = os.path.expanduser(os.path.expandvars(models_dir))
    if batch_size is None:
        batch_size = 1
    assert nsamples % batch_size == 0
    enc = encoder.get_encoder(model_name, models_dir)
    hparams = model.default_hparams()
    with open(os.path.join(models_dir, model_name, 'hparams.json')) as f:
        hparams.override_from_dict(json.load(f))
    if length is None:
        length = hparams.n_ctx // 2
    elif length > hparams.n_ctx:
        raise ValueError("Can't get samples longer than window size: %s" % hparams.n_ctx)
    with tf.Session(graph=tf.Graph()) as sess:
        context = tf.placeholder(tf.int32, [batch_size, None])
        np.random.seed(seed)
        tf.set_random_seed(seed)
        output = sample.sample_sequence(
            hparams=hparams, length=length,
            context=context,
            batch_size=batch_size,
            temperature=temperature, top_k=top_k, top_p=top_p
        )
        saver = tf.train.Saver()
        ckpt = tf.train.latest_checkpoint(os.path.join(models_dir, model_name))
        saver.restore(sess, ckpt)
        context_tokens = enc.encode(raw_text)
        generated = 0
        for _ in range(nsamples // batch_size):
            out = sess.run(output, feed_dict={
                context: [context_tokens for _ in range(batch_size)]
            })[:, len(context_tokens):]
            for i in range(batch_size):
                generated += 1
                text = enc.decode(out[i])
                print("==========")
                print("Before splitlines: " + text)
                print("==========")
                pika = text.splitlines()[0]
                stripes = pika.encode(encoding=sys.stdout.encoding,errors='ignore')
                tigger = stripes.decode("utf-8")
                mew = str(tigger)
                meow = regex(mew)
                if learn == True:
                    learning = raw_text + meow + " "
                update.message.reply_text(meow) 
                print("==========")
                mod = str(mode)
                print("Mode: " + mod)
                lear = str(learn)
                print("Learn: " + lear)
                lent = str(length)
                print("Length: " + lent)
                print("==========")
                ball = str(pika)
                print("Before regex: " + ball)
                print("==========")
                print("Output: " + meow)
                print("==========")
                print("Raw_text or Original: " + raw_text)
                print("==========")
                print("Learning text or Next: " + learning)
                print("==========")
    sess.close()
def error(bot, update):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("BOTFATHERBOTKEYTOKEN", use_context=False)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("chatbot", chatbot))
    dp.add_handler(CommandHandler("finish", finish))
    dp.add_handler(CommandHandler("learnon", learnon))
    dp.add_handler(CommandHandler("learnoff", learnoff))
    dp.add_handler(CommandHandler("learnreset", learnreset))
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, runn))
    # log all errors
    dp.add_error_handler(error)
    # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    fire.Fire(main)
