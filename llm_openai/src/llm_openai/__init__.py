import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

# Load your API key from an environment variable or secret management service

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_KEY"))


def main() -> int:
    completion = client.chat.completions.create(
        model="gpt-4o", 
        messages=[{"role": "user",
                   "n": 1,
                   "temperature": 0.0, # most deterministic results
                   "content": "What do I do when Emacs goes to the background and I can't access it?"}])
    print(f"\nCompletion:\n\n{completion.choices[0].message.content}")
    print(f"Token use for completion: {completion.usage}")
    return 0
