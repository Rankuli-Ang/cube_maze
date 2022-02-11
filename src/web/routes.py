from src import app
from flask import render_template


@app.route("/")
def home_page():
    return "<p>Hello, World!</p>"