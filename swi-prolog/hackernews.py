from urllib.request import Request, urlopen
import json
from bs4 import BeautifulSoup
from pprint import pprint

def get_new_stories(anAgent={'User-Agent': 'PythonAiBook/1.0'}):
    req = Request("https://hacker-news.firebaseio.com/v0/newstories.json",
                  headers=anAgent)
    httpResponse = urlopen(req)
    data = httpResponse.read()
    #print(data)
    ids = json.loads(data)
    #print(ids)
    # just return the most recent 3 stories:
    return ids[0:3]

ids = get_new_stories()

def get_story_data(id, anAgent={'User-Agent': 'PythonAiBook/1.0'}):
    req = Request(f"https://hacker-news.firebaseio.com/v0/item/{id}.json",
                  headers=anAgent)
    httpResponse = urlopen(req)
    return json.loads(httpResponse.read())

def get_story_text(a_uri, anAgent={'User-Agent': 'PythonAiBook/1.0'}):
    req = Request(a_uri, headers=anAgent)
    httpResponse = urlopen(req)
    soup = BeautifulSoup(httpResponse.read())
    return soup.get_text()

for id in ids:
    story_json_data = get_story_data(id)
    pprint(story_json_data)
    if 'url' in story_json_data:
        print(get_story_text(story_json_data['url']))