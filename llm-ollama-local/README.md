# llm-ollama-local

Use local LLM models served by Ollama

## Installing library for this project locally on your computer

    make install_local

Then to use it:

```
$ python
Python 3.12.2 | packaged by Anaconda, Inc. | (main, Feb 27 2024, 12:57:28) [Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import llm_ollama_local
>>> llm_ollama_local.completion("what is 1 + 2? Be concise and just return a number")
{'model': 'llama3:latest', 'created_at': '2024-07-09T22:57:35.366004Z', 'response': '3', 'done': True, 'done_reason': 'stop', 'context': [128006, 882, 128007, 271, 12840, 374, 220, 16, 489, 220, 17, 30, 2893, 64694, 323, 1120, 471, 264, 1396, 128009, 128006, 78191, 128007, 271, 18, 128009], 'total_duration': 2977166084, 'load_duration': 2800033709, 'prompt_eval_count': 25, 'prompt_eval_duration': 143336000, 'eval_count': 2, 'eval_duration': 31780000}
'3'
>>> 
```