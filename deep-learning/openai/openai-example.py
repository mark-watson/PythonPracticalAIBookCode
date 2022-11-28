# from OpenAI's documentation

import os

import openai

openai.api_key = os.environ.get('OPENAI_KEY')

# list engines
engines = openai.Engine.list()

# print the first engine's id
print(engines.data[0].id)

# create a completion
completion = openai.Completion.create(engine="ada", prompt="What is the capital of France?")

# print the completion
print(completion.choices[0].text)

