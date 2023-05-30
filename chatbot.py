import os
import openai
from googletrans import Translator
from telegram import Update 
from telegram.ext import MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, filters

openai.api_key = "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"
translator = Translator()

content = ""

messages = [
    {"role": "system", "content": content}
]





async def message(update: "Update", context: "ContextTypes.DEFAULT_TYPE"):
    content = update.message.text
    messages.append({"role": "user", "content": content})

    # Detect the language and translate it to English
    detected_lang = translator.detect(content).lang
    translated_text = translator.translate(content, dest='en').text

        # Send the translated text to ChatGPT
    messages.append({"role": "user", "content": translated_text})

    completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

    chat_response = completion.choices[0].message['content']
    # Translate the chat response back to the user's language
    translated_response = translator.translate(chat_response, dest=detected_lang).text
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text=translated_response)

async def start(update: "Update", context: "ContextTypes.DEFAULT_TYPE"):
    await context.bot.send_message(chat_id=update.effective_chat.id, text = "Salam!")

if __name__ == "__main__":
    application = ApplicationBuilder().token('6204736079:AAHAsoU31mU8RAkOLuy92BAazLUBlsjQlXc').build()
    
    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), message)
    application.add_handler(message_handler)

    application.run_polling()



