#!/usr/bin/env python3
"""
Main application file for shyam-development-proj
A Flask web application demonstrating basic functionality.
"""

from flask import Flask, render_template

flaskapp = Flask(__name__)


@flaskapp.route('/')
def home():
  """Home page route."""
  return render_template('home.html')


@flaskapp.route('/about')
def about():
  """About page route."""
  return render_template('home.html')


if __name__ == "__main__":
  flaskapp.run(host="0.0.0.0", port=5000, debug=True)
