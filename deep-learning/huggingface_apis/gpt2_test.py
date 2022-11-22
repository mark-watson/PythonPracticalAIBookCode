import json
import requests
import os
from pprint import pprint

API_URL = "https://api-inference.huggingface.co/models/gpt2"
HF_API_TOKEN = os.environ.get('HF_API_TOKEN')
headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}

def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

data = query("Can you please let us know more details about your ")

pprint(data)

