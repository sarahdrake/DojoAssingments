
from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = "sarahdrake"

import random

@app.route('/')
def index():
    if "win_number" not in session:
        session['win_number'] = random.randrange(0, 100)
    return render_template('index.html')
@app.route('/game', methods = ['POST'])
def game():
    session['guess'] = int(request.form['guess'])
    if session['guess'] == int(session['win_number']):
        session['result'] = str(session['win_number']) + " is the lucky number! You Won!"
    if session['guess'] > int(session['win_number']):
        session['result'] = "Your guess is too high!"
    if session['guess'] < int(session['win_number']):
        session['result'] = "Your guess is too low. Try again!"
    return redirect('/')
@app.route('/win', methods = ['POST'])
def win():
    session.pop('win_number')
    session.pop('result')
    return redirect('/')
app.run(debug=True)
