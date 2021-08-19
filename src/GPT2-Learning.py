#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json, os, string, sys, threading, random, model, sample, encoder, logging, time
import numpy as np
import tensorflow as tf
import re
import os

# Enable console logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Console output debug prints
debug = True

# Session timeout
timeout = 1500

# top_p (refer to gpt-2 documentation)
top = 0.66

# Temperature (refer to gpt-2 documentation)
degree = 1

# Top_p multiplier - add to top_p per word 
# 0.00375‬ - may be shorter
# 0.00400
# 0.00425
# 0.00450
# 0.00475
# 0.00500 - may be longer
mx = 0.00375

# Top_K unused here, might be useful eventually.
tok = 0

# This is the start of the learning cache, could be useful eventually.
learning = ""

# End settings
mode = True
learn = True
user = ""
cache = ""
running = False
temps = str(degree)
tpstring = str(top)

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.

def start(bot, update):
    """Send a message when the command /start is issued."""
    global running
    global mode
    global learn
    global user
    global tim
    global learning
    global cache
    if user == "":
        user = update.message.from_user.id
        mode = True
        learn = True
        learning = ""
        cache = ""
        if mode == True and learn == True:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M. I am in the learning chatbot mode.')
        if mode == True and learn == False:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M I am in the chatbot mode.')
        if mode == False:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M I am in the finishsentence mode.')
        return
    if user == update.message.from_user.id:
        mode = True
        learn = True
        learning = ""
        cache = ""
        if mode == True and learn == True:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M. I am in the learning chatbot mode.')
        if mode == True and learn == False:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M I am in the chatbot mode.')
        if mode == False:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M I am in the finishsentence mode.')
        return
    else:
        left = str(tim)
        update.message.reply_text('Bot is currently in use, make sure to set your settings when their timer runs down. ' + left + ' seconds.')

def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Just type a message... It could be lagged out. /chatbot goes into Me: You: mode. /finish just finishes the text /learnon for conversation learning mode.')

def chatbot(bot, update):
    """Send a message when the command /chatbot is issued."""
    global running
    global mode
    global learn
    global user
    global tim
    global learning
    global cache
    if user == "":
        user = update.message.from_user.id
        mode = True
        learn = False
        learning = ""
        cache = ""
        if mode == True and learn == True:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M. I am in the learning chatbot mode.')
        if mode == True and learn == False:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M I am in the chatbot mode.')
        if mode == False:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M I am in the finishsentence mode.')
        return
    if user == update.message.from_user.id:
        mode = True
        learn = False
        learning = ""
        cache = ""
        if mode == True and learn == True:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M. I am in the learning chatbot mode.')
        if mode == True and learn == False:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M I am in the chatbot mode.')
        if mode == False:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M I am in the finishsentence mode.')
        return
    else:
        left = str(tim)
        update.message.reply_text('Bot is currently in use, make sure to set your settings when their timer runs down. ' + left + ' seconds.')

def finish(bot, update):
    """Send a message when the command /finish is issued."""
    global running
    global mode
    global learn
    global user
    global tim
    global learning
    global cache
    if user == "":
        user = update.message.from_user.id
        mode = False
        learn = False
        learning = ""
        cache = ""
        if mode == True and learn == True:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M. I am in the learning chatbot mode.')
        if mode == True and learn == False:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M I am in the chatbot mode.')
        if mode == False:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M I am in the finishsentence mode.')
        return
    if user == update.message.from_user.id:
        mode = False
        learn = False
        learning = ""
        cache = ""
        if mode == True and learn == True:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M. I am in the learning chatbot mode.')
        if mode == True and learn == False:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M I am in the chatbot mode.')
        if mode == False:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M I am in the finishsentence mode.')
        return
    else:
        left = str(tim)
        update.message.reply_text('Bot is currently in use, make sure to set your settings when their timer runs down. ' + left + ' seconds.')

def learnon(bot, update):
    """Send a message when the command /learnon is issued."""
    global running
    global mode
    global learn
    global user
    global tim
    global learning
    global cache
    if user == "":
        user = update.message.from_user.id
        mode = True
        learn = True
        learning = ""
        cache = ""
        if mode == True and learn == True:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M. I am in the learning chatbot mode.')
        if mode == True and learn == False:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M I am in the chatbot mode.')
        if mode == False:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M I am in the finishsentence mode.')
        return
    if user == update.message.from_user.id:
        mode = True
        learn = True
        learning = ""
        cache = ""
        if mode == True and learn == True:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M. I am in the learning chatbot mode.')
        if mode == True and learn == False:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M I am in the chatbot mode.')
        if mode == False:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M I am in the finishsentence mode.')
        return
    else:
        left = str(tim)
        update.message.reply_text('Bot is currently in use, make sure to set your settings when their timer runs down. ' + left + ' seconds.')

def learnoff(bot, update):
    """Send a message when the command /learnoff is issued."""
    global running
    global mode
    global learn
    global user
    global tim
    global learning
    global cache
    if user == "":
        user = update.message.from_user.id
        mode = True
        learn = False
        learning = ""
        cache = ""
        if mode == True and learn == True:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M. I am in the learning chatbot mode.')
        if mode == True and learn == False:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M I am in the chatbot mode.')
        if mode == False:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M I am in the finishsentence mode.')
        return
    if user == update.message.from_user.id:
        mode = True
        learn = False
        learning = ""
        cache = ""
        if mode == True and learn == True:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M. I am in the learning chatbot mode.')
        if mode == True and learn == False:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M I am in the chatbot mode.')
        if mode == False:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M I am in the finishsentence mode.')
        return
    else:
        left = str(tim)
        update.message.reply_text('Bot is currently in use, make sure to set your settings when their timer runs down. ' + left + ' seconds.')

def learnreset(bot, update):
    """Send a message when the command /learnreset is issued."""
    global running
    global mode
    global learn
    global user
    global tim
    global learning
    global cache
    if user == "":
        user = update.message.from_user.id
        mode = True
        learn = True
        learning = ""
        cache = ""
        if mode == True and learn == True:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M. I am in the learning chatbot mode.')
        if mode == True and learn == False:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M I am in the chatbot mode.')
        if mode == False:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M I am in the finishsentence mode.')
        return
    if user == update.message.from_user.id:
        mode = True
        learn = True
        learning = ""
        cache = ""
        if mode == True and learn == True:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M. I am in the learning chatbot mode.')
        if mode == True and learn == False:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M I am in the chatbot mode.')
        if mode == False:
            update.message.reply_text('Send a message! Get it computed! 1558M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 1558M I am in the finishsentence mode.')
        return
    else:
        left = str(tim)
        update.message.reply_text('Bot is currently in use, make sure to set your settings when their timer runs down. ' + left + ' seconds.')

def regex(mew):
    meow = mew
    if "You:" in meow:
        meow = meow[0:meow.find('You:')]
        if "Me:" in meow:
            meow = meow[0:meow.find('Me:')]
        return meow
    if "Me:" in meow:
        meow = meow[0:meow.find('Me:')]
        if "You:" in meow:
            meow = meow[0:meow.find('You:')]
        return meow
    if "?" in meow:
        meow = meow[0:meow.find('?')]
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
    meow = "Error."
    return meow


def retry(bot, update):
    retr = True
    new = retr
    comput = threading.Thread(target=wait, args=(bot, update, new,))
    comput.start()

def runn(bot, update):
    retr = False
    new = retr
    comput = threading.Thread(target=wait, args=(bot, update, new,))
    comput.start()

def wait(bot, update, new):
    global tim
    global user
    global running
    global mode
    global learn
    global learning
    global cache
    if user == "":
        user = update.message.from_user.id
    if user == update.message.from_user.id:
        user = update.message.from_user.id
        temp = timeout
        compute = threading.Thread(target=interact_model, args=(bot, update, new,))
        compute.start()
        if running == False:
            while temp > 1:
                running = True
                time.sleep(1)
                temp = temp - 1
            if running == True:
                mode = False
                learn = False
                learning = ""
                cache = ""
                user = ""
                update.message.reply_text('Timer has run down, bot has been reset into the default mode.')
                running = False
    else:
        left = str(temp)
        update.message.reply_text('Bot is in use, current cooldown is: ' + left + ' seconds.')

def interact_model(bot, update, new):
    model_name = '1558M'
    seed = random.randint(1431655765, 2863311530)
    nsamples = 1
    batch_size = 1
    top_k = tok
    topp = top
    models_dir = 'models'
    tex = str(update.message.text)
    global learning
    global learn
    global mode
    global cache
#############################################
    # This does some basic length processing.
    if mode == True:
        tlen = len(tex.split())
        if tlen > 300:
            update.message.reply_text('Input text is too long.')
            return
        if new == True and cache:
            m = re.search('.* You: ', cache)
            raw_text = m.group(0)
            tlensp = len(raw_text.split())
            tlen = tlensp - 2   
            length = tlen
            if tlen < 20:
                length = 20
            if tlen > 20:
                length = 20
            if tlen > 30:
               length =  40
            if tlen > 50:
                length = 60
            if debug == True:
                print("Cache is...")
                print(raw_text)
        if new != True:
            texm = 'Me: ' + tex
            initial = texm + ' You: '
            raw_text = learning + initial
            length = tlen
            if tlen < 20:
                length = 20
            if tlen > 20:
                length = 20
            if tlen > 30:
               length =  40
            if tlen > 50:
                length = 60
            cache = raw_text
        maxls = len(raw_text.split())
        if maxls > 300:
            while maxls > 300:
                if debug == True:
                    print("Reducing memory of chat.")
                raw_text = raw_text.split(' Me:', 1)[-1]
                raw_text = "Me:" + raw_text
                maxls = len(raw_text.split())
                if maxls > 300:
                    if debug == True:
                        print("Reducing memory of chat.")
                    raw_text = raw_text.split('You:', 1)[-1]
                    raw_text = "You:" + raw_text
                    maxls = len(raw_text.split())
            if debug == True:
                print("FINAL MEMORY REDUCTION:")
                print(raw_text)
    if mode == False:
        tlen = len(penguin.split())
        length = tlen
        if length > 300:
            update.message.reply_text('Input text is too long.')
            return
        if new != True:
            cache = tex
        if new == True and cache:
            tex = cache
            length = len(tex.split())
            tlen = length
            if debug == True:
                print("Cache is...")
                print(penguin)
        raw_text = tex
    toppf = float(topp)
    lengthm = float(tlen)
    multf = float(mx)
    lxm = float(lengthm * multf)
    top_p = lxm + toppf
    # The max here is 0.84 and minimum 0.005
    if top_p > 0.84:
        top_p = 0.84
    if top_p < 0.005:
        top_p = 0.005
#############################################
    update.message.reply_text('Computing...')
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
            temperature=degree, top_k=top_k, top_p=top_p
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
                if debug == True:
                    print("==========")
                    print("Raw output: " + text)
                    print("==========")
                if mode == True:
                    splitted = text.splitlines()[0]
                else:
                    splitted = text
                encodedstr = splitted.encode(encoding=sys.stdout.encoding,errors='ignore')
                decodedstr = encodedstr.decode("utf-8")
                final = str(decodedstr)
                # disable any regex on finishsentence mode.
                if mode == True:
                    # Final regex
                    sanitized = regex(final)
                    finalsan = " ".join(re.split("[^a-zA-Z.,?!'*]+", sanitized))

                else:
                    finalsan = final
                if learn == True:
                    learning = raw_text + finalsan + " "
                update.message.reply_text(finalsan)
                if debug == True:
                    modes = str(mode)
                    print("Chatbot mode: " + modes)
                    learns = str(learn)
                    print("Learning mode: " + learns)
                    lengths = str(length)
                    print("Length: " + lengths)
                    print("==========")
                    splits = str(splitted)
                    print("Before regex: " + splits)
                    print("==========")
                    print("Output: " + finalsan)
                    print("==========")
                    print("Raw_text or Original: " + raw_text)
                    print("==========")
                    print("Learning text or Next: " + learning)
                    print("==========")
                    tps = str(top_p)
                    print("Final top_p: " + tps)
                    print("==========")
                    print("top_p in: " + tpstring)
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
    updater = Updater("BOTKEY", use_context=False)
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
    dp.add_handler(CommandHandler("retry", retry))
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
    main()
