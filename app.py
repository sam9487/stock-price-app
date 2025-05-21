from flask import Flask, request, render_template
import yfinance as yf
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/price')
def get_price():
    symbol = request.args.get('symbol', 'AAPL')
    start = request.args.get('start', '2023-01-01')
    end = request.args.get('end', '2023-12-31')

    try:
        df = yf.download(symbol, start=start, end=end)
        if df.empty:
            return f"找不到代號 {symbol} 的資料", 404
        return df.to_html(classes="table table-bordered", border=0)
    except Exception as e:
        return f"發生錯誤：{str(e)}", 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
