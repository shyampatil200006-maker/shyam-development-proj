#!/usr/bin/env python3
"""
Main application file for shyam-development-proj
A Flask web application demonstrating basic functionality.
"""

from flask import Flask, render_template, jsonify

flaskapp = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': '1200000'
}, {
    'id': 2,
    'title': 'Project Manager',
    'location': 'Navi Mumbai, India',
    'salary': '1800000'
}, {
    'id': 3,
    'title': "SQL Developer",
    'location': 'Navi Mumbai, India',
    'salary': '1500000'
}]


@flaskapp.route('/')
def home():
  """Home page route. with multiple parameters for job list , banking type"""
  return render_template('home.html', availjobs=JOBS, bnktype="Private")


@flaskapp.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  flaskapp.run(host="0.0.0.0", port=5000, debug=True)
