from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# Define a form for entering the user's name
class NameForm(FlaskForm):

    # Text field for the user's name
    # DataRequired() prevents the form from being submitted with an empty name
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')