import urllib.request
import json

# Stock price of apple fpr entire day

# Daily stock price of apple: https://www.bloomberg.com/quote/AAPL:US#http://www.bloomberg.com/markets/api/bulk-time-series/price/AAPL:US?timeFrame=1_DAY

file = urllib.request.urlopen('https://www.bloomberg.com/markets/api/bulk-time-series/price/AAPL:US?timeFrame=1_DAY')
data = json.load(file)
s = 0

for i in data[0]["price"]:
	y = data[0]["price"][s]["dateTime"]
	x = data[0]["price"][s]["value"]
	s = s + 1
	print(y)
	print(x)
	