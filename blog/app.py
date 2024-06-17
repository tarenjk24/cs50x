import os

from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import current_user
from cs50 import SQL
import sqlite3
import re

from helpers import apology, login_required


# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///blog.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


""" user authentication routes """


# Forms
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("Please provide a username.", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("Please provide a password.", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")
    else:
        return render_template("login.html")


# register
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Forget any user_id.
    session.clear()

    if request.method == "POST":
        # Get user name and password.
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Validate user input.
        if not username:
            return apology("must provide username", 400)

        elif not password:
            return apology("must provide password", 400)

        elif not confirmation:
            return apology("must confirm password", 400)

        elif password != confirmation:
            return apology("must confirm password", 400)

        # Query the database to check if the username is already taken.
        existing_user = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(existing_user) != 0:
            return apology("userename taken", 400)

        # Generate a hash of the password.
        hashed_password = generate_password_hash(password)

        # Insert the new user into the database.
        db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)",
            username,
            hashed_password,
        )

        # Query the database for newly inserted user.
        new_user = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Remember user.
        session["user_id"] = new_user[0]["id"]

        # Display success message.
        flash("Registration successful.", "success")
        return redirect("/")
    else:
        return render_template("register.html")


# logout
@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()
    # Redirect user to login form
    return redirect("/")


# delete
@app.route("/remove", methods=["GET", "POST"])
@login_required
def remove():
    """Delete user account"""
    if request.method == "POST":
        # Get user name and password.
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Validate user input.
        if not username:
            return apology("must provide username", 400)
        elif not password:
            return apology("must provide password", 400)
        elif not confirmation:
            return apology("must confirm password", 400)
        elif password != confirmation:
            return apology("passwords must match", 400)

        # Query the database to check if the username is already taken.
        existing_user = db.execute("SELECT * FROM users WHERE username = ?", username)
        if not existing_user:
            return apology("Wrong username", 403)
        else:
            # Get user id.
            user_id_data = db.execute(
                "SELECT id FROM users WHERE username = ?", (username,)
            )
            user_id = user_id_data[0]["id"]
            # Delete user's account and related data from the database.
            db.execute("DELETE FROM cart WHERE user_id = ?", (user_id,))
            db.execute("DELETE FROM users WHERE username = ?", (username,))
            # Display success message.
            flash("Account deleted successfully.", "success")
            session.clear()
            return redirect("/")
    else:
        return render_template("remove.html")



# Submit mail
@app.route("/layout", methods=["POST"])
def subscribe():
    """Submit mail"""

    # Get the mail
    email = request.form.get("mail")
    # Validate the email
    if not email:
        flash("Please enter your email before submitting.", "error")
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        flash("Please enter a valid email address.", "error")
    else:
        # Insert the 'Mail' in the database
        db.execute("INSERT INTO Mail (email) VALUES (?)", email)
        # Display success message.
        flash("Your mail has been submitted successfully. Thank you!", "success")
        # Redirect to the home page
        return redirect("/")


# link routes
@app.route("/aboutus")
def aboutus():
    """render about us template"""
    return render_template("aboutus.html")


@app.route("/delivery_information")
def delivery_information():
    """render about us template"""
    return render_template("deliveryinformation.html")


@app.route("/privacy_policy")
def privacy_policy():
    """render privacy policy template"""
    return render_template("privacypolicy.html")


@app.route("/terms_conditions")
def terms_conditions():
    """render terms condition template"""
    return render_template("termsconditions.html")


@app.route("/comingsoon")
def comingsoon():
    """render coming soon template"""
    return render_template("comingsoon.html")

@app.route("/")
def index():
    """render coming soon template"""
    return render_template("index.html")


@app.route("/article", methods=["GET", "POST"])
def article():
    """Display products details"""

    # Renders them using the 'productdetails.html' template.
    return render_template("article.html")




#  galerie of pitures in data base.


@app.route("/picturedetails")
def picturedetails():
    """render coming soon template"""
    return render_template("picturedetails.html")

#  galerie of pitures in data base.


@app.route("/articledetails")
def articledetails():
    """render coming soon template"""
    return render_template("articledetails.html")


#  galerie of pitures in data base.

@app.route("/galerie")
def galerie():
    """Display shop catalog"""

    return render_template("galerie.html")

#  youtube posts template.

@app.route("/youtube", methods=["GET", "POST"])
def youtube():
    """Display shop catalog"""

    # Renders them using the 'productdetails.html' template.
    return render_template("youtube.html")


@app.route("/post", methods=["GET", "POST"])
@login_required
def post():
    try:
        # Check if the request method is POST
        if request.method == "POST":
            title = request.form.get("title")
            articles = request.form.get("articles")
            categories = request.form.get("categories")
            link = request.form.get("link")

            # Insert the product into the cart in the database
            db.execute(
                "INSERT INTO post (title, articles, categories, link) VALUES (:title, :articles, :categories, :link)",
                title=title,
                articles=articles,
                categories=categories,
                link=link
            )
            # Display success message.
            flash("Added", "success")

    # Log errors
    except Exception as e:
        app.logger.error(f"Error in adding the number: {e}")
        return apology("an error occurred", 500)
    else:
        # Render the product details page
        return render_template("post.html")


@app.route("/update/<id>", methods=["GET", "POST"])
@login_required
def update(id):
    try:
        article_id = int(id)
        # Check if the request method is POST
        if request.method == "POST":
            title = request.form.get("title")
            articles = request.form.get("articles")
            categories = request.form.get("categories")
            link = request.form.get("link")

            # Insert the product into the cart in the databas
            db.execute("UPDATE post SET title = :title, articles = :articles, categories = :categories, link = :link WHERE id = :id",
                title=title,
                articles=articles,
                categories=categories,
                link=link,
                id=id
                )

            # Display success message.
            flash("updated", "success")

    # Log errors
    except Exception as e:
        app.logger.error(f"Error in adding the number: {e}")
        return apology("an error occurred", 500)
    else:
        # Render the product details page
        return render_template("update.html", article_id=article_id)



@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    """Display products details"""
    user_id = session["user_id"]

    #  Query the database for the product details according to its id.
    articles = db.execute("SELECT * FROM post")

    # Print the product details to the console (for debugging purposes).
    print("articles:", articles)

    # Renders them using the 'productdetails.html' template.
    return render_template("profile.html", articles=articles)


