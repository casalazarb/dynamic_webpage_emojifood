# Upload the products from a json file
# ['dishware', 'drink', 'food-asian', 'food-fruit', 'food-marine', 'food-prepared', 'food-sweet', 'food-vegetable']
import json
from cs50 import SQL

with open('/workspaces/36279482/35_f/static/food.json') as f:
    food = json.load(f)

#print(len(food))

# Configure to use sqlite database
db = SQL("sqlite:///emojisfoods.db")

db.execute("CREATE TABLE emojis (emoji_id INTEGER PRIMARY KEY, codes TEXT,\
    name TEXT, img_name TEXT, char TEXT, subgroup TEXT)")

for emoji in food:
    try:
        codes = emoji["codes"]
        #print(codes)
        name = emoji["name"]
        #print(name)
        img_name = emoji["img_name"]
        #print(img_name)
        char = emoji["char"]
        #print(char)
        subgroup = emoji["subgroup"]
        #print(subgroup)

        db.execute("INSERT INTO emojis (codes, name, img_name, char, subgroup)\
            VALUES (?, ?, ?, ?, ?)", codes, name, img_name, char, subgroup)
    except:
        print("Something went wrong.")