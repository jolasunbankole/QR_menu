from flask import Flask, render_template. request
import requests

app = Flask(__name__)

#route add-menu to add a new product to the stock data
@app.route('/add-menu')
def add_menu():
    #return the add-menu page
    return render_template('menu.html')

@app.route('/add-menu', methods=['POST'])
def add_product():
    # add the new product to the stock data
    product = {
        "Name": request.form['Name'],
        "Price": request.form['Price']
    }
    requests.post('http://menu:5000/add-menu', json=product, timeout=5)
    return {"status":"ok"}

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0", port=5000)