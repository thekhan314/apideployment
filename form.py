from flask_wtf import FlaskForm
from wtforms import StringField, DateField

class JobEntry(FlaskForm):
    role = StringField('Role')
    company = StringField('Company')
    date = DateField('Date')
    url = StringField('URL')
    noes = StringField('Notes')