from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


# Define a form for entering the user's name
class NameForm(FlaskForm):

    # Text field for the user's name
    # DataRequired() prevents the form from being submitted with an empty name
    name = StringField('What is your name?', validators=[DataRequired()])

    # Text field for the user's UofT email address
    email = StringField(
        'What is your UofT Email address?',
        validators=[DataRequired(), Email()]
    )

    submit = SubmitField('Submit')