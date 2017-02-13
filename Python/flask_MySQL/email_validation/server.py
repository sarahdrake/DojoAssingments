from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'emailsdb')
app.secret_key = "Thisissecret!"
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process', methods=['POST'])
def submit():
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    else:
        flash("Success!")
        query = 'INSERT INTO users(email, created_at) VALUES (:email, NOW())'
        data = {'email': request.form['email']}
        mysql.query_db(query, data)
        print request.form['email']
        return redirect('/success')
@app.route('/success', methods=['GET'])
def success():
    query = 'SELECT * FROM users'
    users = mysql.query_db(query)
    return render_template('success.html', all_users_emails=users )
app.run(debug=True)
