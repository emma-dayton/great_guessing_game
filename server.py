from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '5d1ae80a79cc70d7e7e8f4bbe44d6883'
# our index route will handle rendering our form

# session['count'] = 0

@app.route('/')
def index
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
