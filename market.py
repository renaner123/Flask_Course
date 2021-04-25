from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

""" @app.route('/about/<username>')
def about(username):
    return f'<h1> This is the about page of {username}' """k