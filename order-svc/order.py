from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/get-stock')
def get_stock():
    stock_data = requests.get('http://selection:5000/get-stock', timeout=5)
    data = stock_data.json()
    return render_template('menu.html', stock=data['stock'].values(), show_header=show_header)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)