import pykrx.stock as pystock

stock = pystock.get_market_cap('2022-12-29', '2023-07-18', '096640')
print(stock)