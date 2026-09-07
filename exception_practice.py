

import json

try:
    with open("task.json","r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    print("File not found.")
