from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    message = StringField('message', validators=[DataRequired()])
    #lastname = StringField('lastname', validators=[DataRequired()])
    shift = IntegerField('shift')