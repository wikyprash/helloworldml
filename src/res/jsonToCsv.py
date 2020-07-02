import json
import csv

with open('..\\data.json') as jsonFile:
    data = json.load(jsonFile)

print(data)