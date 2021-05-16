import json
import os
from os.path import exists


def read_json():
    json_file = {}
    if os.path.exists('ad.json'):
      with open('ad.json', 'r', encoding='utf8') as f:
        json_file = json.load(f)
        return json_file
   


