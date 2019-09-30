# GPT2-Telegram-Chatbot
GPT2 Telegram chatbot that's been relatively tuned.

Please see the python file.

Install gpt-2 as normal,
Place this file in src/
Install python-telegram-bot through python pip
Input your bot key in the python file.

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

Example of learning mode:
```
OUTPUTS
learning:Me:Hello there! You: This chat is going to be OPEN and OPPORTUNITY FREE.
meow: This chat is going to be OPEN and OPPORTUNITY FREE.
Raw_text:Me:Hello there! You:
Length:17
OUTPUTS
INPUTS
learning:Me:Hello there! You: This chat is going to be OPEN and OPPORTUNITY FREE.
meow: Still Null
Raw_text:Me:Hello there! You: This chat is going to be OPEN and OPPORTUNITY FREE. Me:Really? Cool! You:
Length:17
INPUTS
```
