# Modules
from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

# In house
from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///emojisfoods.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/login", methods=["GET", "POST"])
def login():
    """ Log in an existing user """
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("You must provide a username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("You must provide a password", 403)

        # Query database for username
        the_user = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct check_password_hash() for comparing hashes
        if len(the_user) != 1 or not check_password_hash(the_user[0]["password"], request.form.get("password")):
            return apology("Invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = the_user[0]["user_id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """ Register a new user """
    # If the method is GET go to rendered template register
    if request.method == "GET":
        return render_template("register.html")

    # If the method is POST get the data that the user wrote in the form
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("Username input is blank please write a username")

        if not password:
            return apology("Password input is blank please write a password")

        if not confirmation:
            return apology("Please confirm your password")

        if password != confirmation:
            return apology("Password and confirmation do not match")

        # To insert the password as a hash not a text itself
        hashed_password = generate_password_hash(password)

        # Insert the password as a hash into the table users if user already exists shows apology
        try:
            new_user = db.execute("INSERT INTO users (username, password) VALUES (?, ?)",\
                 username, hashed_password)
        except:
            return apology("That username is already taken")

        # To enter directly to the web page once the user has been registered
        session["user_id"] = new_user

        # This is the access
        return redirect("/")


@app.route("/logout")
def logout():
    """ Log out from the app """
    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/")
@login_required
def index():
    """Show the categories of emojifood available"""
    # The session has the user id and it is an integer
    user_id = session["user_id"]

    # This value is for the unsername to appear in every html to the right side of the signer
    username = db.execute("SELECT username FROM users WHERE user_id = ?", user_id)[0]["username"]

    return render_template("index.html", username=username)

# Emoji food subcategories
# ['dishware', 'drink', 'food-asian', 'food-fruit', 'food-marine', 'food-prepared', 'food-sweet', 'food-vegetable']

@app.route("/dishware")
@login_required
def dishware():
    """Show menu dishware"""
    user_id = session["user_id"]

    username = db.execute("SELECT username FROM users WHERE user_id = ?", user_id)[0]["username"]

    # Query to display subcategory
    list_dishware = db.execute("SELECT * FROM emojis WHERE subgroup = ? ORDER BY name", "dishware")

    return render_template("dishware.html", list_subgroup=list_dishware, username=username)

@app.route("/drinks")
@login_required
def drinks():
    """Show menu drinks"""
    user_id = session["user_id"]

    username = db.execute("SELECT username FROM users WHERE user_id = ?", user_id)[0]["username"]

    # Query to display subcategory
    list_drinks = db.execute("SELECT * FROM emojis WHERE subgroup = ? ORDER BY name", "drink")

    return render_template("drinks.html", list_subgroup=list_drinks, username=username)

@app.route("/asian")
@login_required
def asian():
    """Show menu asian"""
    user_id = session["user_id"]

    username = db.execute("SELECT username FROM users WHERE user_id = ?", user_id)[0]["username"]

    # Query to display subcategory
    list_asian = db.execute("SELECT * FROM emojis WHERE subgroup = ? ORDER BY name", "food-asian")

    return render_template("asian.html", list_subgroup=list_asian, username=username)

@app.route("/fruit")
@login_required
def fruit():
    """Show menu fruit"""
    user_id = session["user_id"]

    username = db.execute("SELECT username FROM users WHERE user_id = ?", user_id)[0]["username"]

    # Query to display subcategory
    list_fruit = db.execute("SELECT * FROM emojis WHERE subgroup = ? ORDER BY name", "food-fruit")

    return render_template("fruit.html", list_subgroup=list_fruit, username=username)

@app.route("/marine")
@login_required
def marine():
    """Show menu marine"""
    user_id = session["user_id"]

    username = db.execute("SELECT username FROM users WHERE user_id = ?", user_id)[0]["username"]

    # Query to display the subcategory
    list_marine = db.execute("SELECT * FROM emojis WHERE subgroup = ? ORDER BY name", "food-marine")

    return render_template("marine.html", list_subgroup=list_marine, username=username)

@app.route("/prepared")
@login_required
def prepared():
    """Show menu prepared"""
    user_id = session["user_id"]

    username = db.execute("SELECT username FROM users WHERE user_id = ?", user_id)[0]["username"]

    # Query to display the subcategory
    list_prepared = db.execute("SELECT * FROM emojis WHERE subgroup = ? ORDER BY name", "food-prepared")

    return render_template("prepared.html", list_subgroup=list_prepared, username=username)

@app.route("/sweets")
@login_required
def sweets():
    """Show menu sweets"""
    user_id = session["user_id"]

    username = db.execute("SELECT username FROM users WHERE user_id = ?", user_id)[0]["username"]

    # Query to display the subcategory
    list_sweets = db.execute("SELECT * FROM emojis WHERE subgroup = ? ORDER BY name", "food-sweet")

    return render_template("sweets.html", list_subgroup=list_sweets, username=username)

@app.route("/vegetable")
@login_required
def vegetable():
    """Show menu vegetable"""
    user_id = session["user_id"]

    username = db.execute("SELECT username FROM users WHERE user_id = ?", user_id)[0]["username"]

    # Query to display the subcategory
    list_vegetable = db.execute("SELECT * FROM emojis WHERE subgroup = ? ORDER BY name", "food-vegetable")

    return render_template("vegetable.html", list_subgroup=list_vegetable, username=username)

@app.route("/metadata", methods=["POST"])
@login_required
def display_metadata():
    """Display the metadata of selected emojis"""
    user_id = session["user_id"]

    username = db.execute("SELECT username FROM users WHERE user_id = ?", user_id)[0]["username"]

    # The variable codes stores the hexadecimal code sent by submit_meta in each subcategory html
    if request.method == "POST":
        codes=request.form['submit_meta']

        item_metadata = db.execute("SELECT * FROM emojis WHERE codes = ?", codes)[0]

        return render_template("metadata.html", item_metadata=item_metadata, username=username)

@app.route("/play")
@login_required
def play():
    """Let's play trivia"""
    user_id = session["user_id"]

    username = db.execute("SELECT username FROM users WHERE user_id = ?", user_id)[0]["username"]

    # Stores the name and img_name of a random emoji to play, db.execute returns a list of dictionaries
    random_emoji = db.execute("SELECT name, img_name FROM emojis ORDER BY RANDOM() LIMIT 1")[0]

    emoji_name = random_emoji["name"]

    emoji_img = random_emoji["img_name"]

    return render_template("play.html", username=username, emoji_name=emoji_name, emoji_img=emoji_img)


@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    """Change the Password"""
    user_id = session["user_id"]

    username = db.execute("SELECT username FROM users WHERE user_id = ?", user_id)[0]["username"]

    # If the method is GET go to rendered template register
    if request.method == "GET":
        return render_template("account.html", username=username)

    # If the method is POST get the data that the user wrote in the form
    else:
        user_id = session["user_id"]
        old_password_db = db.execute("SELECT * FROM users WHERE user_id = ?", user_id)[0]
        old_password_db = old_password_db["password"]

        old_password = request.form.get("old_password")
        new_password = request.form.get("new_password")
        confirmation = request.form.get("confirmation")

        # To compare passwords as a hash

        if not check_password_hash(old_password_db, request.form.get("old_password")):
            return apology("Old password is not correct")

        if not old_password:
            return apology("Old password input is empty")

        if not new_password:
            return apology("New password input is empty")

        if not confirmation:
            return apology("Please confirm your new password")

        if new_password != confirmation:
            return apology("Password and confirmation do not match")

         # To insert the password as a hash not a text itself
        new_hashed_password = generate_password_hash(new_password)

        # Insert the password as a hash into the table userd of the finance database
        try:
            db.execute("UPDATE users SET password = ? WHERE user_id = ?", new_hashed_password, user_id)
        except:
            return apology("Something went wrong")

        # This is the access
        return redirect("/")