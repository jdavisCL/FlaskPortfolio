from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/ascii')
def ascii():
    return render_template('ascii.html')

@app.route('/code')
def code():
    return render_template('code.html')


app.run(debug = True)