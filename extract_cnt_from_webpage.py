import urllib    #it is python 
import re


sym = ["aapl","apy","goog","nflx"]
i=0

while i<len(sym):
	url ="http://finance.yahoo.com/q?s="+sym[i]+"&ql=1"
	htmlfile=urllib.urlopen(url)
	htmltext=htmlfile.read()
	reg='<span id="yfs_184_'+sym[i]+'">(.+?)</span>'
	pat=re.compile(reg)
	price=re.findall(pat,htmltext)
	print 'price of ',sym[i],' is :',price
	i+=1
