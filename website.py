#!/usr/bin/env python3
from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ThisIsATest'

@app.route("/")
def index():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    return render_template('aboutme.html', title='Aboute Me')


@app.route('/projects')
def programmation():
    return render_template('projects.html', title='Projects')

@app.route('/events')
def roadtrip():
    return render_template('events.html', title='Events')

@app.route('/experiences')
def passions():
    return render_template('experiences.html', title='Experiences')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/')
    return render_template('login.html', title='Sign In', form=form)

'''@app.route("/python")
def hello():
    return "Hello World aaaaaaaaaaa!"

@app.route("/members")
def members():
    return "Members"

@app.route("/members/<string:name>/")
def getMember(name):
    return name

@app.route("/hello/<string:name>/")
def helloName(name):
    #return render_template(
    #    'test.html',name=name)

    quotes = [ "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
               "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
               "'To understand recursion you must first understand recursion..' -- Unknown",
               "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
               "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
               "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  ]
    randomNumber = randint(0,len(quotes)-1)
    quote = quotes[randomNumber]

    return render_template(
        'test.html',**locals())
'''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
