import requests
import boto3
from flask import Flask, request, jsonify, render_template
from bs4 import BeautifulSoup

application = app = Flask(__name__)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('products')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webscrape', methods=['POST'])
def webscrape():
    url = request.json['url']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    products = soup.find_all(class_='product_pod')
    data = {}

    for product in products:
        title = product.find('h3').find('a').get('title')
        price = product.find(class_='price_color').get_text().replace('Â', '')
        data[title] = price

    saveToDatabase(data)
    return jsonify(data)


def saveToDatabase(data):
    for title, price in data.items():
        table.put_item(
            Item={
                'ID': title,
                'Price': price
            }
        )


if __name__ == '__main__':
    app.debug = True
    app.run()
