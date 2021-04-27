from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
    # author (string), validator makes this textbox required & label says author
    author = StringField('author', validators=[DataRequired()])
    # message (string), validator makes this textbox required & label says message
    message = StringField('message', validators=[DataRequired()])
    # submit (button), label says 'Send'
    submit = SubmitField('Send')
