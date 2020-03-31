![Rosetta Stone Chatbot](header.png "Rosetta Stone Chatbot")
## GPT2-Telegram-Chatbot

GPT2 Telegram chatbot that's been relatively tuned for chatting. It could probably pass a turing test easily and I'd love for to get it turing test certified eventually. Feel free to make me PRs and I'll check out your code!

For a demo if it's online:
https://telegram.me/finishsentencebot

### Installation/How to use:

1. Install gpt-2 as normal IE:

```python3 -m pip install tensorflow```

or

```python3 -m pip install tensorflow-gpu```

...

```python3 -m pip install -r requirements.txt```

2. Place this file in the src/ folder.

3. Install python-telegram-bot with 

```python3 -m pip install python-telegram-bot```

4. Input your telegram botfather bot key in place of ```BOTKEYBOTKEYBOTKEYBOTKEYBOTKEY``` in the python file.

5. run: ```python3 src/GPT2-Learning.py```

If needed create a shell script that loops the bot python3 command in case of crashes. The bot requires atleast 8GB of free memory, (16GB preferred and a dual-core processor.) 

### For quick command reference:

```
start - Basic start command.
help - Show quick help command.
chatbot - Chatbot mode, me+you string edit and open-ended questions.
finish - Default finish sentence command counting words as output length.
learnon - Turn on sentence compilation with Me+you string for conversation.
learnoff - Turn off the sentnce compilation.
learnreset - Reset the learned conversation.
```

### Example of learning mode backend:
```
INFO:tensorflow:Restoring parameters from models/774M/model.ckpt
2019-10-16 20:05:55,273 - tensorflow - INFO - Restoring parameters from models/774M/model.ckpt
==========
Before splitlines:  I'm in the middle of an internship! I'm a new intern here at Wh
==========
==========
Mode: True
Learn: True
Length: 17
==========
Before regex:  I'm in the middle of an internship! I'm a new intern here at Wh
==========
Output:  I'm in the middle of an internship!
==========
Raw_text or Original: Me: Hi there! My name is Pikachu, how are you today? You: Hello?  Me: Heya! What's up? You:
==========
Learning text or Next: Me: Hi there! My name is Pikachu, how are you today? You: Hello?  Me: Heya! What's up? You: I'm in the middle of an internship!
==========
INFO:tensorflow:Restoring parameters from models/774M/model.ckpt
2019-10-16 20:08:00,910 - tensorflow - INFO - Restoring parameters from models/774M/model.ckpt
==========
Before splitlines:  Interning is a great way to learn about a company and make some great connections!
==========
==========
Mode: True
Learn: True
Length: 17
==========
Before regex:  Interning is a great way to learn about a company and make some great connections!
==========
Output:  Interning is a great way to learn about a company and make some great connections!
==========
Raw_text or Original: Me: Hi there! My name is Pikachu, how are you today? You: Hello?  Me: Heya! What's up? You: I'm in the middle of an internship! Me: Oh that sounds fun! What's the internship about? You:
==========
Learning text or Next: Me: Hi there! My name is Pikachu, how are you today? You: Hello?  Me: Heya! What's up? You: I'm in the middle of an internship! Me: Oh that sounds fun! What's the internship about? You: Interning is a great way to learn about a company and make some great connections!
==========
```

For a list of grammarly scores please see [/SCORES.MD](/SCORES.md).

Here's a example without the learning mode, that will need more work in the future.. I belive this was set with the learning mode off and a top_p of 0.01 before a variable top_p was coded in:

```
You're a smelly tiger plush! I need to give you a bath.
Computing...
I'm not a smelly tiger plush.
Reply:
Yes you are! Hurry up and get in the bathtub, the water is warm!
Computing...
I'm not going to the bathtub, I'm going to the kitchen.
Reply:
Hey! You better get back here!
Computing...
I'm not going anywhere!
Reply:
Then get in the bath tub!
Computing...
I'm not going to get in the bath.
```





***Inspired by the book When HARLIE Was One by David Gerrold***

[![HitCount](http://hits.dwyl.io/TwistedIO/GPT2-Telegram-Chatbot.svg)](http://hits.dwyl.io/TwistedIO/GPT2-Telegram-Chatbot)
