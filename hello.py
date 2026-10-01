# Import the Flask class from the flask package
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def index():
    # Return a simple HTML heading to the browser
    return '<h1>Hello World!</h1>'