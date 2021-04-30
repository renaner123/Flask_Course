from market import app
from flask import render_template
from market.models import Item
from market.forms import RegisterForm

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

""" @app.route('/about/<username>')
def about(username):
    return f'<h1> This is the about page of {username}' """

@app.route('/market')
def market_page():
    items = Item.query.all()

    return render_template('market.html',items=items)

@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('register.html', form=form)

@app.route('/login')
def login_page():
    return render_template('login.html')