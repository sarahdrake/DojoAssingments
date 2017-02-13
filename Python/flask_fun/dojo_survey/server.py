from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    n = request.form['name']
    loc = request.form['location']
    lang = request.form['language']
    c = request.form['comment']
    return render_template("result.html", name = n, location = loc, language = lang, comment = c)
app.run(debug=True)
