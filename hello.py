# Import the Flask class from the flask package
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def index():
    # Return a simple HTML heading to the browser
    return '<h1>Hello World!</h1>'

# Define a dynamic route that accepts a username from the URL
@app.route('/user/<name>')
def user(name):
    # Display the username in the webpage
    return '<h1>Hello, %s!</h1>' % name