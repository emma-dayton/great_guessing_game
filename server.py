from flask import Flask, render_template, request, redirect, session
from random import randint
app = Flask(__name__)
app.secret_key = '5d1ae80a79cc70d7e7e8f4bbe44d6883'
# our index route will handle rendering our form


@app.route('/')
def index():
    if 'num' not in session:
        session['num'] = randint(1,100)
    return render_template("index.html")

@app.route('/try_num', methods=['POST'])
def try_num():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/play_again')
def new_game():
    session.pop('num')
    session.pop('guess')
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
