#!/usr/bin/python3
"""
write a script that adds all args to a Python list,
and then saves them to a file
"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import json
import sys


jason = json.dumps(sys.argv[1:])

with open('add_item.json', 'w') as file:
    file.write(jason)

with open('add_item.json', 'r') as file:
    print(json.load(file))
