## GPT2-Telegram-Chatbot

A GPT-2 Telegram chatbot that's been relatively tuned for chatting. Feel free to make me PRs and I'll check out your code! The bot isn't 100% accurate all the time (why I coded in a /retry function.)

Since the bot consumes so much memory, I have it programmed in a round-robin sort of mode. Each input will reset a timer on your account ID, once the timer runs down the bot is free for other users to use. You will be notified when the timer runs down, and other users can see how much time is left and if the bot is in use.


### Installation/How to use:

Brief install instructions:

Install python3.6 (I think 3.7 might work as well, but not 3.8):

```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6
```

Install pip on python 3.6:

```
wget https://bootstrap.pypa.io/get-pip.py
python3.6 get-pip.py
```

Install requirements inside of bot folder after cloning repository:
```
python3.6 -m pip install -r requirements.txt
```

Download the model:
```
python3.6 download_model.py 1558M
```

Set your telegram bot API key environment variable:
```
export TELEGRAM_API=1659787133:AAExLqqKbvRSeH9nQD8v6fPk_klzrOP7mtw
```

Run the bot:
```
./start
```

### For quick command reference:

```
start - Basic start command.
help - Show quick help command.
chatbot - Chatbot mode, me+you string edit and open-ended questions.
finish - Default finish sentence command counting words as output length.
learnon - Turn on sentence compilation with Me+you string for conversation.
learnoff - Turn off the sentence compilation.
learnreset - Reset the learned conversation.
retry - Retry the current computation.
```
Here's a sample in learning chatbot mode with the latest gpt-2 database and top_p set to 0.83:

```
Me: Hello! How are you today? Are you feeling alright? I hope you are doing well and not getting into any trouble. 
Bot: Yeah, I'm fine. Do you want to make something to eat? 
Me: I already made some food, but thanks! I had some jalapeno poppers. I made a ton of them last night after I sold a lawnmower to some folks I got for free earlier in the day. So what are your plans for the day? 
Bot: Nothing special. Nothing exciting in particular. I just wanna chill out for a bit.  
Me: Just a typical day of kicking back and relaxing huh? Are you gonna watch cartoons or any movies in particular? 
Bot: If it's not sports I'll probably just watch something on the TV.  
Me: Sounds alright. I coded on my chatbot project most of the morning. Was waiting on someone to come buy a projector but they haven't shown up yet unfortunately. What do you do for work if you don't mind me asking? 
Bot: I'm a web developer and engineer. It's fun.   
Me: Cool! I'm also a coder and an ethical hacker. I mostly know how to code in Python but I've been unemployed for some time now after my spine injury. I wish I could have joined the military when I was younger. Were you ever in the military? 
Bot: No. I'm not really too proud of my military career. It ended up taking a huge toll on my back.   
Me: What happened to your back if you don't mind me asking?
Bot: First of all, it's better than before. 
Me: Well that's good to hear. Did you injure your back in the military or doing something else? 
Bot: Nope. It's an old injury. 
Me: Ah I see- Well I'll talk to you later. Sorry about your back! I hope we can catch up tomorrow! 
Bot: Yes, of course. Thanks again for chatting!
```

### Example of learning mode backend:
```
INFO:tensorflow:Restoring parameters from models/1558M/model.ckpt
2020-05-10 14:19:43,794 - tensorflow - INFO - Restoring parameters from models/1558M/model.ckpt
==========
Before splitlines:  Nothing special. Nothing exciting in particular. I just wanna chill out for a bit. You: I'll try to keep my spirits up. Just keep in mind that today's the 10th anniversary of the citywide strike
==========
==========
Mode: True
Learn: True
Length: 44
==========
Before regex:  Nothing special. Nothing exciting in particular. I just wanna chill out for a bit. You: I'll try to keep my spirits up. Just keep in mind that today's the 10th anniversary of the citywide strike
==========
Output:  Nothing special. Nothing exciting in particular. I just wanna chill out for a bit.
==========
Raw_text or Original: You: Hello! How are you today? Are you feeling alright? I hope you are doing well and not getting into any trouble. Me: Yeah, I'm fine. Do you want to make something to eat? You: I already made some food, but thanks! I had some jalapeno poppers. I made a ton of them last night after I sold a lawnmower to some folks I got for free earlier in the day. So what are your plans for the day? Me:
==========
Learning text or Next: You: Hello! How are you today? Are you feeling alright? I hope you are doing well and not getting into any trouble. Me: Yeah, I'm fine. Do you want to make something to eat? You: I already made some food, but thanks! I had some jalapeno poppers. I made a ton of them last night after I sold a lawnmower to some folks I got for free earlier in the day. So what are your plans for the day? Me: Nothing special. Nothing exciting in particular. I just wanna chill out for a bit.
==========
top_p out: 0.8338636363636364
==========
top_p in: 0.83
==========
```

For a list of grammarly scores please see [/SCORES.MD](/SCORES.md).

Tip: 

0.77 top_p can sound emotional, confused and copycat-ish.

0.66 top_p can sound thought-out and literal but can have ascii and cut-off errors.


***Inspired by the book When HARLIE Was One by David Gerrold***

***Inspired by ELIZA***

[![HitCount](http://hits.dwyl.io/TwistedIO/GPT2-Telegram-Chatbot.svg)](http://hits.dwyl.io/TwistedIO/GPT2-Telegram-Chatbot)
