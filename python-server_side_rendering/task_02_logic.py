#!/usr/bin/python3
"""Build a basic Flask application that serves a web page"""
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        data = json.load(file)
    data_items = data.get("items", [])
    return render_template('items.html', items=data_items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
