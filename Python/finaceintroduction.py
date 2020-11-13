import pandas as pd 
import numpy as np
import yfinance as yf
import datetime as dt
from matplotlib import pyplot as plt
from pandas_datareader import data as pdr

yf.pdr_override()

stock=input("Enter a stock ticker symbol: ")

startyear=2019
startmonth=1
startday=1

start=dt.datetime(startyear,startmonth,startday)

now=dt.datetime.now()

df=pdr.get_data_yahoo(stock,start,now)


ma=50

smaString="Sma_" + str(ma)

df[smaString]=df.iloc[:,4].rolling(window=ma).mean()


df=df.iloc[ma:]

numH=0
numC=0

for i in df.index:
    if(df["Adj Close"][i] > df[smaString][i]):
        numH+=1
    else:
        numC+=1


# data to plot
n_groups = 1
means_frank = (numH)
means_guido = (numC)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.2
opacity = 0.8

rects1 = plt.bar(index, means_frank, bar_width,
alpha=opacity,
color='k',
label='closed HIGH')

rects2 = plt.bar(index + bar_width, means_guido, bar_width,
alpha=opacity,
color='r',
label='closed LOW')

plt.xlabel('From 2019 to today')
plt.ylabel('amount of close')
plt.title('HIGH vs LOW' + ' ' + stock + ' ' + 'close')
plt.xticks(index + bar_width, (''))
plt.legend()

plt.tight_layout()
plt.show()

#print("close is higher: " + str(numH) + " times")
#print("close is higher: " + str(numC) + " times")


