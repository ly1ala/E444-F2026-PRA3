from flask import Flask, render_template, redirect, url_for, session, request
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
            # Store the submitted name and email in the session
            session['name'] = submitted_name
            session['email'] = submitted_email

            # Redirect the user to the chatbot page
            return redirect(url_for('chatbot'))
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
# Display the chatbot page
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

# Process messages sent to the chatbot
@app.route('/chat', methods=['POST'])
def chat():
    message = request.json['message']

    # Remember the user's name
    if message.lower().startswith('my name is '):
        remembered_name = message[11:].strip().rstrip('.')
        session['remembered_name'] = remembered_name
        reply = f'Nice to meet you, {remembered_name}!'

    # Recall the user's name
    elif 'what is my name' in message.lower():
        if 'remembered_name' in session:
            reply = f"Your name is {session['remembered_name']}."
        else:
            reply = "I don't know your name yet."

    elif 'hello' in message.lower():
        reply = 'Hello!'

    else:
        reply = "I don't understand."

    return {'reply': reply}

# Log out and clear the chatbot's remembered information
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))