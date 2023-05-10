import os
import openai
from googletrans import Translator

openai.api_key = "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"
translator = Translator()

content = ""

messages = [
    {"role": "system", "content": content}
]

while True:
    content = input("You: ")
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

    print("ChatGPT: " + translated_response)
