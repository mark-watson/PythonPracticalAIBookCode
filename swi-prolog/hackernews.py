"Example calling Hacker News APIs from Python"

from urllib.request import Request, urlopen
import json
from bs4 import BeautifulSoup
from pprint import pprint

DEFAULT_AGENT = {"User-Agent": "PythonAiBook/1.0"}

def get_new_stories(an_agent="PythonAiBook/1.0"):
  req = Request("https://hacker-news.firebaseio.com/v0/newstories.json",
                headers={"User-Agent": an_agent})
  with urlopen(req) as http_response:
    data = http_response.read()
    # print(data)
    the_ids = json.loads(data)
    # print(the_ids)
    # just return the most recent 3 stories:
    return the_ids[0:3]

def get_story_data(an_id, an_agent="PythonAiBook/1.0"):
  req = Request(f"https://hacker-news.firebaseio.com/v0/item/{an_id}.json",
                headers={"User-Agent": an_agent})
  with urlopen(req) as http_response:
    return json.loads(http_response.read())


def get_story_text(a_uri, an_agent="PythonAiBook/1.0"):
  req = Request(a_uri, headers={"User-Agent": an_agent})
  with urlopen(req) as http_response:
    soup = BeautifulSoup(http_response.read())
    return soup.get_text()


for story_id in get_new_stories():
  story_json_data = get_story_data(story_id)
  pprint(story_json_data)
  if "url" in story_json_data:
    print(get_story_text(story_json_data["url"]))
