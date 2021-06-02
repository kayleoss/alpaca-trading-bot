# alpaca-trading-bot
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
