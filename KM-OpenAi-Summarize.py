#!/usr/bin/env /Library/Frameworks/Python.framework/Versions/3.11/bin/python3

import openai
import pyperclip
import os

# Retrieve OpenAI API key from environment variable
openai.api_key = os.environ.get('KMVAR_OPENAI_API_KEY')

# Get text from clipboard
text = pyperclip.paste()

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are an excellent summarizer."},
        {"role": "user", "content": f"Summarize the following: {text}"}
    ]
)

# Print the generated text to standard output
print(response.choices[0].message.content.strip())
