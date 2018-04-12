"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from segundoparcial import app, genPrimes

@app.route('/')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Juan Pablo Rodríguez Macías'
    )

@app.route('/prime/<int:number>')
def n(number):
    """Renders the home page."""
    return render_template(
        'number.html',
        number=number,
        numbers=list(genPrimes(number))
    )