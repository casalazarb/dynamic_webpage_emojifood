import random
from cs50 import SQL

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///emojisfoods.db")

number_of_emojis = db.execute("SELECT COUNT(codes) as number_of_emojis FROM emojis")[0]["number_of_emojis"]

random_emoji = random.randint(1, number_of_emojis)

random_sql = db.execute("SELECT name, img_name FROM emojis ORDER BY RANDOM() LIMIT 1")


print(type(number_of_emojis))
print(number_of_emojis)

print(type(random_emoji))
print(random_emoji)

print(random_sql)
