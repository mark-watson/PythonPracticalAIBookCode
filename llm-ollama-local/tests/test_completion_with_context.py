import unittest
import os
from llm_ollama_local import completion_with_context

class TestCompletionWithContext(unittest.TestCase):
    def test_completion_with_context(self):
        # Get the path to the context file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        context_file_path = os.path.join(current_dir, '..', 'context_data', 'science_advisor.txt')

        # Test prompt
        prompt = "What is the theory of relativity?"

        # Call the function
        response = completion_with_context(prompt, context_file_path)

        # Assert that the response is not empty
        self.assertTrue(len(response) > 0)

        # Assert that the response contains relevant keywords
        self.assertTrue('Einstein' in response or 'physics' in response or 'spacetime' in response)

if __name__ == '__main__':
    unittest.main()
