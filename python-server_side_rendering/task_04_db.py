#!/usr/bin/python3
"""Create a flask app that renders an html template"""
from flask import Flask, render_template, request
import json
import csv
import sqlite3


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
    with open('items.json', 'r') as f:
        data = json.load(f)
        items = data.get('items', [])
    return render_template('items.html', items=items)


@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id')
    products = []

    if source not in ["json", "csv", "sql"]:
        return render_template('product_display.html', error="Wrong source")

    if source == "json":
        try:
            with open("products.json", 'r') as f:
                products = json.load(f)
        except FileNotFoundError:
            return render_template('product_display.html', error="Wrong source")

    if source == "csv":
        try:
            with open("products.csv", 'r') as f:
                data = csv.DictReader(f)
                for row in data:
                    products.append(row)
        except FileNotFoundError:
            return render_template('product_display.html', error="Wrong source")

    if source == "sql":
        try:
            connexion = sqlite3.connect("products.db")
            cursor = connexion.cursor()

            if id:
                cursor.execute("SELECT * FROM Products WHERE id = ?", (id,))
                results = cursor.fetchall()
            else:
                cursor.execute("SELECT * FROM Products")
                results = cursor.fetchall()

            if not results:
                return render_template('product_display.html', error="Product not found")
            
            for result in results:
                products.append({
                    "id": result[0],
                    "name": result[1],
                    "category": result[2],
                    "price": result[3]
                })

            return render_template('product_display.html', products=products)

        except sqlite3.Error:
            return render_template('product_display.html', error="Wrong source")
        finally:
                connexion.close()

    if id:
        products = [product for product in products if id == str(product["id"])]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
