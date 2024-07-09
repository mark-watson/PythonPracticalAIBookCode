import pytest
from llm_ollama_local import completion

def test_completion():
    answer = completion("what is 1 + 2? Be concise and just return a number")
    print(answer)
    assert answer == "3"