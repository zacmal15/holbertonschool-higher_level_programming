#!/usr/bin/python3
"""Flask app that displays items from a json file."""

import json
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    """Display the home page."""
    return render_template("index.html")


@app.route("/about")
def about():
    """Display the about page."""
    return render_template("about.html")


@app.route("/contact")
def contact():
    """Display the contact page."""
    return render_template("contact.html")

@app.route("/items")
def items():
    """Display items stored in JSON file."""
    with open("items.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    return render_template(
        "items.html",
        items=data.get("items",[])
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)