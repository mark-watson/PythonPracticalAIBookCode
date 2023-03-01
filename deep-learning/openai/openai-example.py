# Using ChatGPT API (from OpenAI's documentation)

import os

import openai

openai.api_key = os.environ.get('OPENAI_KEY')

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": "What do I do when Emacs goes to the background and I can't access it?"}]
)

print(completion)
