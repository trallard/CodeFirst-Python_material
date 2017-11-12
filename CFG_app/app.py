from flask import Flask, render_template, request, redirect, session
from helpers.twitter import *
from helpers.twitter_keys import *


app = Flask("Tweets scraper")
session = {}

@app.route('/')
def index():
    """ This will be the landing page for the app we will be using:
    this is intended to serve as an app accessing and displaying data from
    APIS"""
    return render_template('index.html', title = 'Landing page')

@app.route("/twitter")
def twitter_example():
    return render_template("twitter.html")

@app.route("/twitter_search", methods = ['POST'])
def twitter_search_app():
    session['s'] = request.form['s']
    return redirect()


# "debug=True" causes Flask to automatically refresh upon any changes you
# make to this file.
app.run(debug=True)