import requests
import sys
import time
import csv

with open('tickers', 'rb') as csvfile:
	tReader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for item in tReader:
		tickers = item

# tickers = sys.argv[1].split(",")

for ticker in tickers:
	print(ticker)
	url = "http://ichart.finance.yahoo.com/table.csv?s="+ticker+"&b="+time.strftime("%d")+"&a="+str(int(time.strftime("%m"))-1)+"&c="+str(int(time.strftime("%Y"))-10)+"&e="+time.strftime("%d")+"&d="+str(int(time.strftime("%m"))-1)+"&f="+time.strftime("%Y")+"&g=d&ignore=.csv"
	oFile = "data\\"+ticker+".csv"
	r = requests.get(url, stream=True)
	chunk_size = 1024

	with open(oFile, 'wb') as fd:
		for chunk in r.iter_content(chunk_size):
			fd.write(chunk)
