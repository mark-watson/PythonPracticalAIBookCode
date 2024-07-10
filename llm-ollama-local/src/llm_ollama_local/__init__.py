import ollama

# Initialize the Ollama client
client = ollama.Client()

# Specify the model name and input text
model_name = "llama3:latest"

def completion(prompt: str) -> str:
    response = client.generate(model_name, prompt)
    #print(response)
    return response['response']

def completion_with_context(prompt: str, context_file_path: str) -> str:
    with open(context_file_path, 'r') as file:
        context = file.read()
    
    full_prompt = f"Context:\n{context}\n\nPrompt:\n{prompt}"
    response = client.generate(model_name, full_prompt)
    print(response)
    return response['response']

