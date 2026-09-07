import json
from flask import Flask, request

app = Flask(__name__)

stock_data = {'stock': 
    {"Coffee": {"Name": "cappuccino", "Price": 3.5}}
}

#route get-stock to return json data of stock_data
@app.route('/get-stock')
def get_stock():
    # return the stock data as a JSON response
    data = json.dumps(stock_data)
    return data 

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

@app.route('/add-menu', methods=['POST'])
def add_menu():
    # get the product data from the request body
    product = {
        "Name": request.json['Name'],
        "Price": request.json['Price']
    }
    key = request.json['Name'] + '_' + request.json['Price']
    stock_data['stock'][key] = product
    return {"status":"ok"}