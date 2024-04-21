<<<<<<< HEAD
# Emojifoods
#### Video Demo:
#### Description:

Inspired by Jennifer 8 Lee's amazing emoji talk, I decided to begin my final project to
help anyone who, like me, struggles to understand what each food emoji represents.

Because emojis are mostly used in cellphones, the images are quite small. I was mostly
interested in the food category, especially because there are so many delicious but
exotic foods. I am from Colombia in Latin America, and our Asian population is very small,
so most people here are unfamiliar with this type of food.

It has been a total pleasure for me to learn a lot of things, such as the fact that
we do not have an orange in the fruit subcategory, but rather a tangerine, but most
people think they are sending an orange. And what about that strange star-shaped white
thing with a pink swirl? Surprisingly, that delicacy is a slice of narutomaki, a type
of fish cake used as a topping for ramen soup in Japan; the official emoji name is
"fish cake with swirl," and it belongs to the emojis' Asian food subcategory.

## Folders of the project:

### The preprocess folder contains:

count.py and counts.py contains auxiliary codes to check some queries from the emojisfoods.db
database and check the number of items registered.

food_json.py creates a json file with the metadata of the emojis in the food category
using the API found in "https://unpkg.com/emoji.json@14.0.0/emoji.json"

get_img.py downloads the nice emojis images from "https://emojiapi.dev/api/v1/" and
creates the name .png extension of each image used in the page design it is stored
in the static folder /static/images_food/

### The static folder contains:

images_design: images for the webpage layout

images_food: the emoji images

food.json: json file with all the metadata for food emojis

styles.css: file with the code for beautyfication of each element

upload_emojis.py loads with the use of CS50 SQL library the metadata of the emojis to
the emojisfood.db database

### The templates folder contains:

account.html: allows the user to change password

apology.html: renders and apology when something goes wrong

asian.html, dishware.html, drinks.html, fruit.html, marine.html, prepared.html,
sweets.html, vegetable.html: display the emojis in each subcategory

index.html: displays the homepage with the eight subcategories of food emojis.

layout.html: this part appears with all the other pages, it contains the header and
the footer with the credits from the sources

login.html: allows a user already created to log in

metadata.html: displays the metadata for each emoji

play.html: allows the user to test their knowledge in the food emojis subject

register.html: allows a new user to create their account

### Root directory

app.py: contains the flask app.

emojisfoods.db: the database with users and emojis tables

helpers.py: functionalities in python to help other functions, apology() function

README.md: this file

requirements.txt: the libraries and modules needed in python.
=======
# dynamic_webpage_emojifood
Dynamic webpage, displays information about emojies related to food.
>>>>>>> 01d6fb0eedef958083273d90ef2f8c0904261fea
