from flask import render_template, url_for, request, abort, redirect, flash
from randomwebsite import app
import random
from randomwebsite.dadjokes import getJoke

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/dadjokes")
def dadjokes():
    joke = getJoke()
    print(joke.setup)
    print(joke.punchline)
    return render_template("dadjokes.html", joke = joke)

@app.route("/result")
@app.route("/rockpaperscissors")
def rockpaperscissors():
    return render_template("rockpaperscissor.html")
