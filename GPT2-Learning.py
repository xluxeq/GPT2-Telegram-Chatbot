#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import fire, json, os, string, sys, threading, random, model, sample, encoder, logging, time
import numpy as np
import tensorflow as tf

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# You can set the settings here
# Session timeout
timstart = 1200
# Model logic (trained to usually)
top = 0.73
# Temperature
temp = 1
# Length multiplier for top_p
mx = 3
# End settings

temps = str(temp)
tpstring = str(top)
mode = False
learn = False
learning = ""
user = ""
running = False

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
    if user == "":
        user = update.message.from_user.id
        mode = False
        learn = False
        learning = ""
        if mode == True and learn == True:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M. I am in the learning chatbot mode.')
        if mode == True and learn == False:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M I am in the chatbot mode.')
        if mode == False:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M I am in the finishsentence mode.')
        return
    if user == update.message.from_user.id:
        mode = False
        learn = False
        learning = ""
        if mode == True and learn == True:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M. I am in the learning chatbot mode.')
        if mode == True and learn == False:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M I am in the chatbot mode.')
        if mode == False:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M I am in the finishsentence mode.')
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
    if user == "":
        user = update.message.from_user.id
        mode = True
        learn = False
        learning = ""
        if mode == True and learn == True:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M. I am in the learning chatbot mode.')
        if mode == True and learn == False:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M I am in the chatbot mode.')
        if mode == False:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M I am in the finishsentence mode.')
        return
    if user == update.message.from_user.id:
        mode = True
        learn = False
        learning = ""
        if mode == True and learn == True:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M. I am in the learning chatbot mode.')
        if mode == True and learn == False:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M I am in the chatbot mode.')
        if mode == False:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M I am in the finishsentence mode.')
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
    if user == "":
        user = update.message.from_user.id
        mode = False
        learn = False
        learning = ""
        if mode == True and learn == True:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M. I am in the learning chatbot mode.')
        if mode == True and learn == False:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M I am in the chatbot mode.')
        if mode == False:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M I am in the finishsentence mode.')
        return
    if user == update.message.from_user.id:
        mode = False
        learn = False
        learning = ""
        if mode == True and learn == True:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M. I am in the learning chatbot mode.')
        if mode == True and learn == False:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M I am in the chatbot mode.')
        if mode == False:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M I am in the finishsentence mode.')
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
    if user == "":
        user = update.message.from_user.id
        mode = True
        learn = True
        learning = ""
        if mode == True and learn == True:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M. I am in the learning chatbot mode.')
        if mode == True and learn == False:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M I am in the chatbot mode.')
        if mode == False:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M I am in the finishsentence mode.')
        return
    if user == update.message.from_user.id:
        mode = True
        learn = True
        learning = ""
        if mode == True and learn == True:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M. I am in the learning chatbot mode.')
        if mode == True and learn == False:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M I am in the chatbot mode.')
        if mode == False:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M I am in the finishsentence mode.')
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
    if user == "":
        user = update.message.from_user.id
        mode = True
        learn = False
        learning = ""
        if mode == True and learn == True:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M. I am in the learning chatbot mode.')
        if mode == True and learn == False:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M I am in the chatbot mode.')
        if mode == False:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M I am in the finishsentence mode.')
        return
    if user == update.message.from_user.id:
        mode = True
        learn = False
        learning = ""
        if mode == True and learn == True:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M. I am in the learning chatbot mode.')
        if mode == True and learn == False:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M I am in the chatbot mode.')
        if mode == False:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M I am in the finishsentence mode.')
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
    if user == "":
        user = update.message.from_user.id
        mode = True
        learn = True
        learning = ""
        if mode == True and learn == True:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M. I am in the learning chatbot mode.')
        if mode == True and learn == False:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M I am in the chatbot mode.')
        if mode == False:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M I am in the finishsentence mode.')
        return
    if user == update.message.from_user.id:
        mode = True
        learn = True
        learning = ""
        if mode == True and learn == True:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M. I am in the learning chatbot mode.')
        if mode == True and learn == False:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M I am in the chatbot mode.')
        if mode == False:
            update.message.reply_text('Send a message! Get it computed! 774M Settings: Logic: ' + tpstring + ' Rate:' + temps + ' GPT-2 774M I am in the finishsentence mode.')
        return
    else:
        left = str(tim)
        update.message.reply_text('Bot is currently in use, make sure to set your settings when their timer runs down. ' + left + ' seconds.')

def regex(mew):
    meow = mew
    if "Me:" in meow:
        meow = meow[0:meow.find('Me:')]
        return meow
    if "You:" in meow:
        meow = meow[0:meow.find('You:')]
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
    meow = "Error."
    return meow

def runn(bot, update):
    top_p = top
    temperature = temp
    mult = mx
    comput = threading.Thread(target=wait, args=(bot, update, top_p, temperature, mult,))
    comput.start()

def wait(bot, update, top_p, temperature, mult):
    global tim
    global user
    global running
    global mode
    global learn
    global learning
    if user == "":
        user = update.message.from_user.id
    if user == update.message.from_user.id:
        user = update.message.from_user.id
        tim = timstart
        compute = threading.Thread(target=interact_model, args=(bot, update, top_p, temperature, mult,))
        compute.start()
        if running == False:
            while tim > 1:
                running = True
                time.sleep(1)
                tim = tim - 1
            if running == True:
                mode = False
                learn = False
                learning = ""
                user = ""
                update.message.reply_text('Timer has run down, bot has been reset into the default mode.')
                running = False
    else:
        left = str(tim)
        update.message.reply_text('Bot is in use, current cooldown is: ' + left + ' seconds.')

def interact_model(bot, update, top_p, temperature, mult):
    model_name = 'trained'
    seed = random.randint(1, 4294967295)
    nsamples = 1
    batch_size = 1
    top_k = 0
    # Rating of settings I've tried, these were run through grammarly.
    # 0.67 - 99 ! Short responses 19/20 in context
    # 0.69 - 99 ! Repetitive responses 20/20 in context
    # 0.72 - 99 ! Readability 19/20 in context
    # 0.73 - 99 ! Readability 20/20 in context
    # Also set this to like 0.01 it does some crazy stuff. Just the lean mode doesn't work.
    models_dir = 'models'
    tex = update.message.text
    penguin = str(tex)
    global learning
    global learn
    # This does some basic length processing.
    global mode
#############################################
    if mode == True:
        cat = len(penguin.split(" "))
        rng = cat * mult
        length = round(rng)
        wolf = "You: " + penguin
        initial = wolf + " Me:"
        raw_text = learning + initial
    if mode == False:
        cat = len(penguin.split(" "))
        rng = cat * mult
        length = round(rng)
        raw_text = penguin
    tx = float(top_p)
    cax = float(cat)
    lex = float(length)
    ta = ((1-tx)/cax)
    tn = (ta * lex)
    top_p = ((tx) + (ta))
    if top_p > 1:
        top_p = 1
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
                if mode == True:
                    pika = text.splitlines()[0]
                else:
                    pika = text
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
                tps = str(top_p)
                print("top_p out: " + tps)
                print("==========")
                tpa = str(tx)
                print("top_p in: " + tpa)
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
    updater = Updater("TELEGRAMBOTKEYFROMBATFATHER", use_context=False)
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
