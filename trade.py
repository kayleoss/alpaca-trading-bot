import alpaca_trade_api as tradeapi
import time
import os
import requests
from bs4 import BeautifulSoup

'''
This is a trading script that uses alpaca trading to initiate paper trades.

WHAT IT DOES: 
    Gets a list of qualified stocks and submits an order to buy 100 quantities of each, at 10% under market price. 
    Wait 5 seconds after each other to ensure it has enough time to complete the order.

WHICH SYMBOLS QUALIFY:
    The script searches yahoo finance trending symbols and determines if the stock is qualified based on two factors:
    1 - The stock must have a change percentage greater than 5%
    2 - The stock must have a market price below $100

WHERE IT GETS DATA FROM:
    Symbol data is retreived from yahoo finance.
    Stock data is received as real-time data from IEX (the Investors Exchange)

Made by Katie (Duo) Liu
Github: https://github.com/kayleoss
'''

key = os.environ["ALPACA_KEY"]
sec = os.environ["ALPACA_SEC"]
url = "https://paper-api.alpaca.markets"
api = tradeapi.REST(key, sec, url, api_version='v2')
response = requests.get("https://ca.finance.yahoo.com/trending-tickers")
page = BeautifulSoup(response.content, "html.parser")
account_status = api.get_account()
symbols_to_trade = []

def submit_order(symbol, limit_price):
    if account_status.status == "ACTIVE":
        order = api.submit_order(symbol=symbol, qty="100", side="buy", type="limit", limit_price=str(limit_price), time_in_force="day")
        print(order)
    else:
        print(account_status)
        

def get_symbols():
    rows = page.select('tr.simpTblRow')
    for row in rows:
        sym = row.select('a[data-test="quoteLink"]')[0].get_text()
        price = float(row.select('td[aria-label="Last Price"] > span')[0].get_text())
        change_per = float(row.select('td[aria-label="% Change"] > span')[0].get_text().replace("%", "").replace("+", "").replace("-", ""))
        
        if change_per > 5 and price < 100:
            symbol = {
                "symbol": sym,
                "price_limit": int(price) * 0.9
            }
            symbols_to_trade.append(symbol)
        else:
            print(f"YOU AINT BUYIN THIS: {sym}")

get_symbols()

for symbol in symbols_to_trade:
    submit_order(symbol['symbol'], symbol['price_limit'])
    time.sleep(3)