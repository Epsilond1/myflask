# coding: utf-8

"""
FIXME
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
