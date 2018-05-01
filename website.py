#!/usr/bin/env python3
from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'My website'

@app.route("/")
def index():
    return render_template('index.html', title='Home')

@app.route('/')
def about():
    return render_template('index.html', title='Aboute Me')

@app.route('/projects')
def programmation():
    return render_template('projects.html', title='Projects')

@app.route('/events')
def roadtrip():
    return render_template('events.html', title='Events')

@app.route('/experiences')
def passions():
    return render_template('experiences.html', title='Experiences')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
