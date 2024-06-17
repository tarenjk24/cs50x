import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3

from helpers import apology, login_required, lookup, usd


# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Extract user's cash balance and stock account data.
    stocks = db.execute(
        "SELECT symbol, SUM(shares) as total_shares FROM account WHERE user_id = :user_id GROUP BY symbol HAVING total_shares > 0",
        user_id=session["user_id"],
    )

    # Get the user's cash balance.
    cash = db.execute(
        "SELECT cash FROM users WHERE id = :user_id", user_id=session["user_id"]
    )[0]["cash"]

    # Initialize variables for total values.
    total_spending = cash
    overall_total = cash

    # Calculate stock values and update total values.
    for stock in stocks:
        symbol = stock["symbol"]
        total_shares = stock["total_shares"]

        # Fetch stock quote.
        quote = lookup(symbol)
        if quote:
            stock["price"] = quote["price"]
            stock["value"] = stock["price"] * total_shares
            total_spending += stock["value"]
            overall_total += stock["value"]

    # Render the HTML template with the calculated data.
    return render_template(
        "index.html",
        stocks=stocks,
        cash=cash,
        total_spending=total_spending,
        overall_total=overall_total,
    )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        # Get symbol and shares.
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")

        # Validate symbol and shares.
        if not symbol:
            return apology("must provide a symbol", 400)
        elif not shares:
            return apology("must provide shares", 400)
        elif not shares.isdigit() or int(shares) <= 0:
            return apology("invalid  shares", 400)

        # Retrieve stock quote.
        quote = lookup(symbol)

        # Check if valid.
        if quote is None:
            return apology("symbol does not exist", 400)

        # Get price and calculate total cost.
        price = quote["price"]
        cost = int(shares) * price

        # Check if user has enough cash.
        user_cash = db.execute(
            "SELECT cash FROM users WHERE id = :user_id", user_id=session["user_id"]
        )[0]["cash"]
        if user_cash < cost:
            return apology("Low on cash", 400)

        # Update user's cash.
        db.execute(
            "UPDATE users SET cash = cash - :cost WHERE id = :user_id",
            cost=cost,
            user_id=session["user_id"],
        )

        # Insert values to account.
        db.execute(
            "INSERT INTO account (user_id, symbol, shares, price) VALUES (:user_id, :symbol, :shares, :price)",
            user_id=session["user_id"],
            symbol=symbol,
            shares=shares,
            price=price,
        )

        # Display message to user.
        return redirect("/")

        # Redirect user to home page
        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    user_id = session["user_id"]

    # Retrieve user transaction history from the database.
    query = """
        SELECT symbol, SUM(shares) as total_shares, price, transacted
        FROM account
        WHERE user_id = :user_id
        ORDER BY transacted DESC
        """

    rows = db.execute(query, user_id=user_id)

    return render_template("history.html", rows=rows)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

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


@app.route("/remove", methods=["GET", "POST"])
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
            return apology("must confirm password", 400)

        # Query the database to check if the username is already taken.
        existing_user = db.execute("SELECT * FROM users WHERE username = ?", username)
        if not existing_user:
            return apology("Wrong user", 403)
        else:
            # Get user id.
            user_id_data = db.execute(
                "SELECT id FROM users WHERE username = ?", (username,)
            )
            user_id = user_id_data[0]["id"]

            # Delete user's account and related data from the database.
            db.execute("DELETE FROM account WHERE user_id = ?", (user_id,))
            db.execute("DELETE FROM USERS WHERE username = ?", (username,))

            # Display success message.
            flash("Account deleted successfully.", "success")

            # Forget any user_id
            session.clear()

            # Redirect user to login form
            return redirect("/")
    else:
        return render_template("remove.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        # Get symbol
        symbol = request.form.get("symbol")

        # Validate symbol input.
        if not symbol:
            return apology("Must provide symbol", 400)

        # Look for symbol quote.
        quote = lookup(symbol)

        # Check if valid.
        if not quote:
            return apology("Symbol does not exist", 400)

        # If the quote is valid, render the quoted.html template with the stock details.
        return render_template("quoted.html", quote=quote)

    else:
        return render_template("quote.html")


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


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # Fetch the user's stocks from the database
    stocks = db.execute(
        "SELECT symbol, SUM(shares) AS total_shares FROM account WHERE user_id = :user_id GROUP BY symbol HAVING total_shares > 0",
        user_id=session["user_id"],
    )

    if request.method == "POST":
        # Get symbols and shares.
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")

        # Check if valid.
        if not symbol or not shares:
            return apology("Missing symbol and/or missing shares", 400)

        elif not shares.isdigit() or int(shares) <= 0:
            return apology("Invalid shares")

        else:
            shares = int(shares)

        for stock in stocks:
            if stock["symbol"] == symbol:
                if stock["total_shares"] < shares:
                    return apology("not enough shares")
                else:
                    # Look up the current price of the stock.
                    quote = lookup(symbol)

                    if not quote:
                        return apology("Stock quote not found")

                    price = quote["price"]
                    selling_value = price * shares

                    # Update the user's cash.
                    db.execute(
                        "UPDATE users SET cash = cash + :selling_value WHERE id = :user_id",
                        selling_value=selling_value,
                        user_id=session["user_id"],
                    )

                    # Insert a record for the sell transaction in the account table.
                    db.execute(
                        "INSERT INTO account (user_id, symbol, shares, price) VALUES (:user_id, :symbol, :shares, :price)",
                        user_id=session["user_id"],
                        symbol=symbol,
                        shares=-shares,
                        price=price,
                    )

                    # Display success message.
                    flash("Sold!", "success")

                    # Redirect user to index.
                    return redirect("/")
        return apology("symbol not found")

    else:
        return render_template("sell.html", stocks=stocks)
