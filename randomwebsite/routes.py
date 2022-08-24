from flask import render_template, url_for, request, abort, redirect, flash
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired
from randomwebsite import app
import random
from randomwebsite.dadjokes import getJoke
from randomwebsite.key import sec_key

app.config['SECRET_KEY'] = sec_key

rps = ["rock", "paper", "scissors"]

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
        if request.form:
            user_result = request.form['choice']
            ai_result = random.choice(rps)
            if ai_result == "rock" and user_result == "paper":
                won = "You"
            elif ai_result == "paper" and user_result == "scissors":
                won = "You"
            elif ai_result == "scissors" and user_result == "rock":
                won = "You"
            elif ai_result == user_result:
                won = "Nobody"
            else:
                won = "AI"
            print(user_result)
            print(ai_result)
            print(won)
            return render_template("rockpaperscissor.html", result = user_result, airesult = ai_result, won = won)
        else:
            return render_template("rockpaperscissor.html", result = "Did not choose!!!", airesult = "Oviously will be winning!", won = "AI in his greatest mind ")
    else:
        return render_template("rockpaperscissor.html", result = "NONE")

   

@app.route("/<res>")
def result(res):
   return render_template("rockpaperscissor.html", result = res)
    
