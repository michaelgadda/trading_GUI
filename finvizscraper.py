import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from tkinter import filedialog, Text, simpledialog, Label
def findImpInfoOnTicker():
    search_ticker = simpledialog.askstring("Enter Ticker", "Please input the ticker that you would like to pull data for:")


    finviz  = 'https://finviz.com/quote.ashx?t={}'
    finviz_ticker = finviz.format(search_ticker)
    print(finviz_ticker)

    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}


    source = requests.get(finviz_ticker, headers = agent)
    qf = pd.read_html(source.text, header=0)
    soup = BeautifulSoup(source.content,'lxml')

    dataTable = soup.find('table', class_="snapshot-table2")

    row1 = dataTable.find_all('tr', class_="table-dark-row" )[0]
    row2 = dataTable.find_all('tr', class_="table-dark-row" )[1]
    row3 = dataTable.find_all('tr', class_="table-dark-row" )[2]
    row4 = dataTable.find_all('tr', class_="table-dark-row" )[3]
    row5 = dataTable.find_all('tr', class_="table-dark-row" )[4]
    row6 = dataTable.find_all('tr', class_="table-dark-row" )[5]
    row7 = dataTable.find_all('tr', class_="table-dark-row" )[6]
    row8 = dataTable.find_all('tr', class_="table-dark-row" )[7]


    marketCapColumn = row2.find_all('td')[1]
    marketCap = marketCapColumn.find('b').get_text()

    floatColumn = row2.find_all('td')[9]
    float = floatColumn.find('b').get_text()

    shortFloatColumn = row3.find_all('td')[9]
    shortFloat = shortFloatColumn.find('b').get_text()

    atrColumn = row8.find_all('td')[11]
    atr = atrColumn.find('b').get_text()

    instOwnColumn = row3.find_all('td')[7]
    instOwn = instOwnColumn.find('b').get_text()

    print("Market Cap: " + str(marketCap))
    print("Float: " + str(float))
    print("Short Float: " + str(shortFloat))
    print("ATR: " + str(atr))
    print("Inst Own: " + str(instOwn))

    list = [marketCap,float,shortFloat,atr,instOwn]
    return list;



