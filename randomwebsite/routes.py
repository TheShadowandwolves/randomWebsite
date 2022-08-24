from flask import render_template, url_for, request, abort, redirect, flash
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired
from randomwebsite import app
import random
from randomwebsite.dadjokes import getJoke
from randomwebsite.key import sec_key

app.config['SECRET_KEY'] = sec_key

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


@app.route("/rockpaperscissors" , methods=["POST", "GET"])
def rockpaperscissors():
    if request.method == "POST":
        result = request.form['choice']
        print(result)
        return render_template("rockpaperscissor.html", result = result)
    else:
        return render_template("rockpaperscissor.html", result = "NONE")

   

@app.route("/<res>")
def result(res):
   return render_template("rockpaperscissor.html", result = res)
    
