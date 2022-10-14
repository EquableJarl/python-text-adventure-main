import yaml
import json

with open("data.json", 'r') as j:
    data_dict = json.loads(j.read())

with open("data.yml", 'w') as y:
    yaml.dump(data_dict, y)
