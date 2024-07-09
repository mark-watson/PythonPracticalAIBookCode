import ollama

# Initialize the Ollama client
client = ollama.Client()

# Specify the model name and input text
model_name = "llama3:latest"

def completion(prompt: str) -> str:
    response = client.generate(model_name, prompt)
    print(response)
    return response['response']

