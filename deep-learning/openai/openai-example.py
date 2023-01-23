# from OpenAI's documentation

import os

import openai

openai.api_key = os.environ.get('OPENAI_KEY')

# create a completion
input_text = "Mary went to the grocery store. She bought"
completion = openai.Completion.create(engine="davinci",
                                      prompt=input_text)

# print the completion
print(completion.choices[0].text)

