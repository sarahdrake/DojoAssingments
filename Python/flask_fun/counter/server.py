from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = "ThisIsMySuperSecretKeyJelly"
@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template('index.html')

@app.route('/ninja')
def plus2():
    session['count'] += 1
    return redirect('/')
@app.route('/hacker')
def reset():
    session['count'] = 0
    return redirect('/')
app.run(debug=True)
