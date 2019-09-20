from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired


class Login(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    room = StringField('Room name', validators=[DataRequired()])
    submit = SubmitField('Enter')



