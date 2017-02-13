from flask import Flask
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'twitter')
print mysql.query_db("SELECT * FROM faves")
app.run(debug=True)
