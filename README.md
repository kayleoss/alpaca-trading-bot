# alpaca-trading-bot
This is a trading script that uses alpaca trading to initiate paper trades.

WHAT IT DOES: 
    Gets a list of qualified stocks and submits an order to buy 100 quantities of each, at 10% under market price. 
    Wait 3 seconds after each other to ensure it has enough time to complete the order.

WHICH SYMBOLS QUALIFY:
    The script searches yahoo finance trending symbols and determines if the stock is qualified based on two factors:
    1 - The stock must have a change percentage greater than 5%
    2 - The stock must have a market price below $100

WHERE IT GETS DATA FROM:
    Symbol data is retreived from yahoo finance.
    Stock data is received as real-time data from IEX (the Investors Exchange)
    
TO USE THIS SCRIPT:
    You have to sign up for alpaca free trading account: https://alpaca.markets/docs/trading-on-alpaca/market-data/
    And get an API key and secret from the paper trading tab which you can save to your environment variables as ALPACA_KEY and ALPACA_SEC

Made by Katie (Duo) Liu
Github: https://github.com/kayleoss
