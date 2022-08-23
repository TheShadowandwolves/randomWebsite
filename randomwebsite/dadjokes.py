from flask import render_template, url_for, request, abort, redirect, flash
import random
import json
import requests

class Joke:
    def __init__(self, setup, punchline, author, nswf):
        self.setup = setup
        self.punchline = punchline
        self.author = author
        self.nswf = nswf

url = "https://dad-jokes.p.rapidapi.com/random/joke"

headers = {
	"X-RapidAPI-Key": "5d27c56599msh50538298144a3dcp197319jsne9f3cbd6ab37",
	"X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)


def getJoke():
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    setup = data["body"][0]["setup"]
    punchline = data["body"][0]["punchline"]
    author = data["body"][0]["author"]["name"]
    nswf = data["body"][0]["NSFW"]
    joke = Joke(setup, punchline, author, nswf)
    return joke
