from flask import Flask, render_template, flash, redirect
from config import Config
from forms import AddAuto

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def welcome_page():
    return render_template('welcome.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/user')
def user():
    return render_template('user.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddAuto()
    if form.validate_on_submit():
        flash('Car added: '.format(
            form.autoName.data, form.autoModel.data, form.engine.data, form.passengers.data))
        return render_template('return.html')
    return render_template('addAuto.html', form=form)


if __name__ == '__main__':
    app.run()
