# from flask import Flask, render_template
# app = Flask(__name__)
# @app.route('/')
#
# def index():
#     return render_template('index.html')
# app.run(debug=True)

# from flask import Flask, render_template
# app = Flask(__name__)
# @app.route('/ninjas')
# def index():
#     return render_template("ninjas.html")
# app.run(debug=True)

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/dojos/new')
def index():
    return render_template("dojos.html")
app.run(debug=True)
