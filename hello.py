# Import Flask and the template rendering function
from flask import Flask, render_template
from datetime import datetime

# Create a Flask application instance
app = Flask(__name__)

# Render the home page with the user's name and current time
@app.route('/')
def index():
    # Get the current date and time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Pass the name and current time to the HTML template
    return render_template(
        'index.html',
        name='Shengya (Lyla) Huang',
        current_time=current_time
    )