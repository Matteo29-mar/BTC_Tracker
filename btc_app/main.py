from flask import Flask, render_template, jsonify
from flask_cors import CORS
import requests
import plotly.graph_objs as go
import plotly.io as pio

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bitcoin-price')
def get_bitcoin_price():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json")
    data = response.json()
    price = data["bpi"]["USD"]["rate"]
    return jsonify({"bitcoin_price": price})

@app.route('/bitcoin-chart')
def bitcoin_chart():
    # Fetch Bitcoin price data for the last 30 days (example URL, adjust as needed)
    response = requests.get("https://api.coindesk.com/v1/bpi/historical/close.json?for=yesterday")
    data = response.json()
    dates = list(data['bpi'].keys())
    prices = list(data['bpi'].values())

    # Create the plotly figure
    fig = go.Figure(data=[go.Scatter(x=dates, y=prices, mode='lines', name='Bitcoin Price')])
    fig.update_layout(title='Bitcoin Price Over the Last 30 Days', xaxis_title='Date', yaxis_title='Price (USD)')
    
    graph_html = pio.to_html(fig, full_html=False)
    
    return render_template('bitcoin_chart.html', graph_html=graph_html)

@app.route('/bitcoin-news')
def bitcoin_news():
    # Example news sources (replace with actual news API calls)
    news = [
        {"title": "Bitcoin hits new all-time high", "url": "https://news.bitcoin.com/bitcoin-hits-new-all-time-high/"},
        {"title": "Why Bitcoin is the future of finance", "url": "https://www.forbes.com/sites/forbesfinancecouncil/2021/01/04/why-bitcoin-is-the-future-of-finance/"},
        {"title": "Bitcoin crashes: What you need to know", "url": "https://www.cnbc.com/2021/05/19/bitcoin-crashes-what-you-need-to-know.html"}
    ]
    return render_template('bitcoin_news.html', news=news)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
