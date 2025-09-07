#!/usr/bin/env python3
"""
Main application file for shyam-development-proj
A Flask web application demonstrating basic functionality.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    """Home page route."""
    return '''
    <h1>Welcome to Shyam Development Project!</h1>
    <p>This is a Flask web application running in Replit.</p>
    <p>The project is working successfully!</p>
    '''

@app.route('/about')
def about():
    """About page route."""
    return '''
    <h1>About</h1>
    <p>This is a Python Flask development project.</p>
    <p>Built and running in the Replit environment.</p>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

