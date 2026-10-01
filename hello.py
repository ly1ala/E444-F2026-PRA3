# Import Flask and the template rendering function
from flask import Flask, render_template
# Import the form created in forms.py
from forms import NameForm


# Create a Flask application instance
app = Flask(__name__)
# Secret key is required by Flask-WTF to protect forms
app.config['SECRET_KEY'] = 'hard-to-guess-string'

# Display and process the name form
@app.route('/', methods=['GET', 'POST'])
def index():

    # Create an instance of the name form
    form = NameForm()

    # Start with no submitted name or email
    name = None
    email = None
    error = None

    # Check whether the form was submitted and passed validation
    if form.validate_on_submit():

        # Get the submitted name and email
        submitted_name = form.name.data
        submitted_email = form.email.data

        # Check whether the email is a UofT email
        if 'utoronto' in submitted_email.lower():
            name = submitted_name
            email = submitted_email

            # Clear the form after successful submission
            form.name.data = ''
            form.email.data = ''
        else:
            error = 'Please fill in a UofT email address.'

    # Send the form and submitted name to the HTML template
    return render_template(
        'index.html',
        form=form,
        name=name,
        email=email,
        error=error
    )