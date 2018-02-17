import urllib.request
import re

urls = ["http://cnn.com","http://nytimes.com","https://timesofindia.indiatimes.com"] # array of urls
i = 0
regex = '<title>(.+?)</title>' # taking all the characters between title tag
pattern = re.compile(regex) # converting regex string to expression that can be interpreted by regex library
while i <3:

	htmlfile = urllib.request.urlopen(urls[i])
	htmltext = htmlfile.read().decode()
	#pattern1 = pattern.decode('utf-8')
	titles = re.findall(pattern,htmltext)
	print(titles)
	#print(htmltext[0:100])# to print first 100 characters of each website
	i = i+1