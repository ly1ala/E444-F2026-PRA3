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

    # Start with no submitted name
    name = None

    # Check whether the form was submitted and passed validation
    if form.validate_on_submit():
        name = form.name.data

        # Clear the form after submission
        form.name.data = ''

    # Send the form and submitted name to the HTML template
    return render_template(
        'index.html',
        form=form,
        name=name
    )