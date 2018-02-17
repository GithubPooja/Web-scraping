import urllib.request

import re


Symbols = open("NASDAQ1.txt") # have downloaded different symbols and saved them in ths same directory where this programming code is written
Symbollist = Symbols.read().split(" ")
print(Symbollist)

for i in Symbollist:
	htmlfile = urllib.request.urlopen("https://www.nasdaq.com/symbol/"+i)
	htmltext = htmlfile.read().decode()



	regex = '<div id="qwidget_lastsale" class="qwidget-dollar">(.+?)</div>'	


	pattern  = re.compile(regex)

	price = re.findall(pattern, htmltext)


	print  (i,'price'.join(price))

