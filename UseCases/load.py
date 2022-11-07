import json


with open('./json_examples/valid_user.json', 'r') as json_file:
    json = json.load(json_file)

    print(json['name'])
