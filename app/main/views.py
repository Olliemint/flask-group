from app import app
from flask import render_template


@app.route('/')
@app.route('/fruits')

def fruits():
    
    return render_template('fruits.html')


@app.route('/veges')

def veges():
    
    return render_template('veges.html')
    
    
    
    