# Import libraries
from urllib.request import urlopen

from urllib.request import urlretrieve

# Import json
import json

def download_img(url, file_path, file_name):
    full_path = file_path + file_name
    urlretrieve(url, full_path)

# Store the URL in url as parameter for urlopen
webpage = 'https://emojiapi.dev/api/v1/'
ext = '/256.png'
file_path = '/workspaces/36279482/35_final/images/'

# Opening JSON file
with open('food.json') as file_json:
    # Returns JSON object as a dictionary
    food = json.load(file_json)

print(len(food))

# Iterating through the json list
not_downloaded = []
number_downloaded = 0
for item in food :
    url = webpage + item['codes'] + ext
    file_name = item['name'].replace(' ', '_') + '.png'
    try:
        download_img(url, file_path, file_name)
        #print(f"{file_name} has been downloaded.")
        number_downloaded += 1
        print(number_downloaded)
    except:
        not_downloaded.append(file_name)
        print(f"{file_name} has not been downloaded.")

print(not_downloaded)

# Opening JSON file
with open('food.json') as file_json:
    # Returns JSON object as a dictionary
    food = json.load(file_json)

downloaded = []
for item in food:
    if item['img_name'] not in not_downloaded:
        downloaded.append(item)
    else:
        continue

print(len(downloaded))

# Save to folder the food,json without the missing emojis
food_json = json.dumps(downloaded, indent=1)
food_file = open("food.json", "w")
food_file.write(food_json)
food_file.close()