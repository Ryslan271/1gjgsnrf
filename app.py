import os
import sqlite3

from flask import Flask, render_template, request, redirect, flash, url_for
from flask_login import login_user, login_required
from forms import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/blogs.sqlite")


@app.route("/")
def home():
    return render_template('Osnova.html')


@app.route("/Lyshee")
@login_required
def lyshee():
    return render_template('Lyshee.html')


@app.route("/O nas")
def onas():
    pass


@app.route("/Contact")
@login_required
def contact():
    return render_template('Contact.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    pass


@app.route('/regist', methods=['GET', 'POST'])
def register():
    pass


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
