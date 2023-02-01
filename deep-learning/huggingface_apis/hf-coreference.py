import json
import requests
import os
from pprint import pprint

# NOTE: Hugging Face does not have a direct anaphora resolution model, so this
#       example is faking it using masking with a BERT model.

HF_API_TOKEN = os.environ.get('HF_API_TOKEN')
headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/bert-base-uncased"

def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

data = query("John Smith bought a car. [MASK] drives it fast.")

pprint(data)

