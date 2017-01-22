import urllib.request
from bs4 import BeautifulSoup
from threading import Thread
import time
import csv

stockList = []



tickerList = ['AAPL','GOOGL']

for ticker in tickerList:
     stockList.append({'ticker': ticker, 'url':'http://www.nasdaq.com/symbol/'+ticker+'/real-time'})
# for stock in stockList:
#     print(stock['ticker'])
#     print(stock['url'])
# urlList = []
# for ticker in tickerList:
#     urlList.append('http://www.nasdaq.com/symbol/'+ticker+'/real-time')

data = open('data.csv','w')
writer = csv.writer(data)
writer.writerow(('ticker','time','price'))
data.close()

def getPrice(ticker,url):
    while True:
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html,'html.parser')
        tag = soup.find(id="qwidget_lastsale")
        price = tag.get_text()[1:]
        data = open('data.csv','w')
        writer = csv.writer(data)
        writer.writerow((ticker,'time',str(price)))
        data.close()
        print(price)



threadList = []
for stock in stockList:
    threadList.append(Thread(target = getPrice, args=(stock['ticker'],stock['url'])))
for thread in threadList:
    thread.start()





# t1 = Thread(target = getPrice1)
# t2 = Thread(target = getPrice2)
# t3 = Thread(target = getPrice, args=(urlList[0],))
#
# t1.start()
# t2.start()
# t3.start()

# threadList = []
#
# for url in urlList:
#     threadList.append(Thread(getPrice(url)))

# for thread in threadList:
#     thread.setDaemon(True)
#     thread.start()



# timerList = []
#
# # for url in urlList:
# #     timerList.append(threading.Timer(1.0,getPrice(url)))
