from flask import Flask
from flask import request, redirect, url_for, flash
from flask import render_template
from wtforms import Form, BooleanField, StringField, PasswordField, validators

users = []


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])


app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name='noob'):
    return render_template('index.html', name=name)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = form.username.data
        users.append(user)
        flash('users so far:{}'" ".join(users))
        return redirect(url_for('/'))
    return render_template('register.html', form=form)


app.run(debug=True, port=8889)
