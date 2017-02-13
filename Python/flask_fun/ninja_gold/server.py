from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "sarahdrake"

import random
from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process_money', methods=['POST'])
def process_money():
    if "gold" not in session:
        session['gold'] = 0
    if "log" not in session:
        session['log'] = ""
    session['choice'] = request.form['building']

    if session['choice'] == 'farm':
        session['farmgold'] = random.randint(10,21)
        session['gold'] = int(session['gold']) + session['farmgold']
        session['log'] += "Earned " + str(session['farmgold']) + " gold from the farm!  " + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "\n"
        print session['gold']

    elif session['choice'] == 'cave':
        session['cavegold'] = random.randint(5,11)
        session['gold'] = int(session['gold']) + session['cavegold']
        session['log'] += "Earned " + str(session['cavegold']) + " gold from the cave!  " + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "\n"
        print session['gold']

    elif session['choice'] == 'house':
        session['housegold'] = random.randint(1,6)
        session['gold'] = int(session['gold']) + session['housegold']
        session['log'] += "Earned " + str(session['housegold']) + " gold from the house!  " + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "\n"
        print session['gold']

    elif session['choice'] == 'casino':
        session['casinogold'] = random.randint(-50,51)
        session['gold'] = int(session['gold']) + session['casinogold']
        session['log'] += "Earned " + str(session['casinogold']) + " gold from the casino!  " + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "\n"
        print session['gold']

    return render_template('index.html')
app.run(debug=True)

### still need to create a clear/pop of all session data to restart (button)
### If statments depending of if you win or loose coins from the casino
