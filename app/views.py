# coding: utf-8

"""
FIXME
"""

from flask import render_template, flash, redirect
from app import app
from forms import LoginForm


class User(object):

    def __init__(self):
        self._LOGIN = None

    def update_login(self, login):
        self._LOGIN = login

    def get_login(self):
        return self._LOGIN


instance_user = User()


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': instance_user .get_login()}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home Page', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        instance_user.update_login(form.openid.data)
        return redirect('/index')

    return render_template('login.html', title='Sign In', form=form)
