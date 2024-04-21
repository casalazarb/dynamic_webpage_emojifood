# https://unpkg.com/emoji.json@14.0.0/emoji.json
# Import libraries
import json
from urllib.request import urlopen

# Store the URL in url as parameter for urlopen
url = 'https://unpkg.com/emoji.json@14.0.0/emoji.json'

# Store the response of URL
response_json= urlopen(url)

# Storing the JSON response from url in data this creates a list of dicts
emojis = json.loads(response_json.read())

# Let's extract only emojis related with food and drinks
SUBGROUPS = ['dishware', 'drink', 'food-asian', 'food-fruit', 'food-marine', 'food-prepared', 'food-sweet', 'food-vegetable']

# Declare a list to store the dictionaries with columns selected
food_drink = []

for sub in SUBGROUPS:
    for item in emojis:
        food = {}
        # Select only food according to subgroups
        if item['group'] == 'Food & Drink' and item['subgroup'] == sub:
            if len(item['codes']) > 5:
                food['codes'] = item['codes'][0:5]
            else:
                food['codes'] = item['codes']
            food['name'] = item['name']
            food['img_name'] = item['name'].replace(' ', '_') + '.png'
            food['char'] = item['char']
            food['subgroup'] = item['subgroup']
            food_drink.append(food)

# Take food_drink list and convert into a json save the file to a folder as food.json
food_json = json.dumps(food_drink, indent=1)
food_file = open("food.json", "w")
food_file.write(food_json)
food_file.close()