from flask import Flask, render_template
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def welcome_page():
    return render_template('welcome.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/user')
def user():
    return render_template('user.html')


if __name__ == '__main__':
    app.run()
