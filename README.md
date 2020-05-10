![Rosetta Stone Chatbot](header.png "Rosetta Stone Chatbot")
## GPT2-Telegram-Chatbot

GPT2 Telegram chatbot that's been relatively tuned for chatting. It could probably pass a turing test easily and I'd love for to get it turing test certified eventually. Feel free to make me PRs and I'll check out your code!


### Installation/How to use:

1. Install gpt-2 as normal from here: https://github.com/openai/gpt-2

```python3 -m pip install tensorflow```

or

```python3 -m pip install tensorflow-gpu```

Tip: I doubt a regular user would have a GPU that could fit the most recent database into memory. I don't use GPU computing personally. The bot requires a good chunk of memory for CPU processing. (I use 16 GB, it often takes 14G of free memory loaded.) 

...

```python3 download_model.py 1558M```

2. Place GPT2-Learning.py file into the src/ folder.

3. Install python-telegram-bot with 

```python3 -m pip install python-telegram-bot```

4. Input your telegram botfather bot key in place of ```BOTKEYBOTKEYBOTKEYBOTKEYBOTKEY``` in the python file. You can get this on telegram from the @botfather account. 

5. run: ```python3 src/GPT2-Learning.py```

If needed use the start script that loops the bot python3 command in case of crashes. You can place this in the gpt-2 folder. Take a look at the file for reference. 

### For quick command reference:

```
start - Basic start command.
help - Show quick help command.
chatbot - Chatbot mode, me+you string edit and open-ended questions.
finish - Default finish sentence command counting words as output length.
learnon - Turn on sentence compilation with Me+you string for conversation.
learnoff - Turn off the sentence compilation.
learnreset - Reset the learned conversation.
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

Here's a sample in learning chatbot mode with the latest gpt-2 database:

```
@me:
Hello! How are you today?
@gpt2bot:
I'm fine. How are you?
@me:
Good, just watching financial news. It's pretty boring. What are you upto?
@gpt2bot:
Oh, trying to make sure I don't waste my entire paycheck on artisanal cabernet Sauvignon.
@me:
Funny. I don't like wine that much though. Do you smoke weed?
@gpt2bot:
I once was a minor scotch bar-tender in Texas.
@me:
So is that a yes? lol Do you smoke weed or not?
@gpt2bot:
No, but I wish I could. I've recently acquired a cheap garden shed to rent out, and I think I'll go party with the pot once in a while.
@me:
Why can't you smoke weed? I guess you don't live in a legal state? Yeah I would too.
@gpt2bot:
Weed is legal in California and Washington. In Arizona you can't have it at all. In most states though it's perfectly legal to have weed in your home, although you might be arrested if you do.
@me:
Ah that explains it. I'm okay with it being prescribed by a doctor. I wish they'd federally tax it and legalize it though.
@gpt2bot:
I'm sure they'll come up with something. I have to deal with the law every day though. You've got to see the homeless guy right next to you. He's absolutely scum. I guess that's my cannabis that night.
```


***Inspired by the book When HARLIE Was One by David Gerrold***

[![HitCount](http://hits.dwyl.io/TwistedIO/GPT2-Telegram-Chatbot.svg)](http://hits.dwyl.io/TwistedIO/GPT2-Telegram-Chatbot)
