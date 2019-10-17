# GPT2-Telegram-Chatbot
GPT2 Telegram chatbot that's been relatively tuned.

Please see the python file.

1. Install gpt-2 as normal,

2. Place this file in src/

3. Install python-telegram-bot through python-pip

4. Input your bot key in the python file.

For quick reference:

```
start - Basic start command.
help - Show quick help command.
chatbot - Chatbot mode, me+you string edit and open-ended questions.
finish - Default finish sentence command counting words as output length.
learnon - Turn on sentence compilation with Me+you string for conversation.
learnoff - Turn off the sentnce compilation.
learnreset - Reset the learned conversation.
```

Example of learning mode backend:
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
## Samples:

### Sample1:
Hi there! My name is Pikachu, how are you today?

I'm doing fine! I'm the most amazing student you'll ever meet!.

That's pretty cool! You're a pokemon trainer?

No, I'm just a student.


### Sample2:
Hi there! My name is Pikachu, how are you today?

Hello?

Heya! What's up?

I'm in the middle of an internship!

Oh that sounds fun! What's the internship about?

Interning is a great way to learn about a company and make some great connections!

#### This is at temperature 1 and top_p of 0.75, the bot sets the length in chatbot mode to full 17-word sentences. When input in this mode is > 1.5 sentences it counts as two sentences or 34 words.
