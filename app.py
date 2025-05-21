from flask import Flask, request, render_template
import yfinance as yf
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_stock', methods=['POST'])
def get_stock():
    symbol = request.form['symbol']
    start = request.form['start']
    end = request.form['end']

    try:
        df = yf.download(symbol, start=start, end=end)
        df.reset_index(inplace=True)
        df['Date'] = df['Date'].astype(str)
        data = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']].to_dict(orient='records')
        return render_template('index.html', stock_data=data, symbol=symbol, start=start, end=end)
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
