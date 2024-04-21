import os
import json

list_files = os.listdir('/workspaces/36279482/35_final/images')

list_files.sort()

#print(list_files)


# Opening JSON file
with open('/workspaces/36279482/35_final/food.json') as file_json:
    # Returns JSON object as a dictionary
    food = json.load(file_json)

list_items = []

for item in food:
    list_items.append(item['img_name'])

list_items.sort()

#print(list_items)

not_there = []
for item in list_files:
    if item in list_items:
        continue
    else:
        not_there.append(item)

print(list_files == list_items)


