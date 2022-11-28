import json
import requests
import os
from pprint import pprint

HF_API_TOKEN = os.environ.get('HF_API_TOKEN')
headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))
    
data = query({"inputs": "The President went to Congress. The Congress was not oblivious of what the Supreme Court's majority had ruled. Even four Justices had found nothing to criticize in the President's requirement that the Federal Government's four-year",
              "parameters": {"do_sample": False},
              "max_length": 12})

pprint(data)
