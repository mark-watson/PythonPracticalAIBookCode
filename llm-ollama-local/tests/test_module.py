import pytest
import os
from llm_ollama_local import completion, completion_with_context

def test_completion():
    answer = completion("what is 1 + 2? Be concise and just return a number")
    print(answer)
    assert answer == "3"

def test_completion_with_context():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    context_file_path = os.path.join(current_dir, '..', 'context_data', 'science_advisor.txt')
    
    prompt = "What is the speed of light? Give a brief answer."
    response = completion_with_context(prompt, context_file_path)
    
    print(response)
    assert len(response) > 0
    assert any(keyword in response.lower() for keyword in ['299,792,458', 'meters per second', 'm/s', 'c'])
