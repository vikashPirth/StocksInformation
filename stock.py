import yfinance as yf
import pandas as pd

symbols = ['NIO', 'NVDA', 'JNJ', 'TSLA']

symbolData = []


for symbol in symbols:
    stock = yf.Ticker(symbol)
    symbolInfo = stock.info
    pd.set_option('display.max_rows', None)

    insiderPurchase = stock.insider_purchases
    cashflowStatement = stock.cashflow
    news = stock.news
    balanceSheet = stock.balance_sheet.iloc[:, 0]


    totalEquity = balanceSheet.get("Stockholders Equity")
    totalLiabilties  = balanceSheet.get('Total Liabilities Net Minority Interest')
    totalAssets = balanceSheet.get('Total Assets')
    totalCurrentAssets =  balanceSheet.get('Current Assets')
    totalCurrentLiabilities = balanceSheet.get('Current Liabilities')
    inventory = balanceSheet.get('Inventory')

    if totalLiabilties and totalEquity :
        dbRatio = totalLiabilties / totalEquity
    else:
        dbRatio = None

    if totalCurrentAssets and totalCurrentLiabilities:
        currentRatio = totalCurrentAssets / totalCurrentLiabilities
    else:
        currentRatio = None 

    if totalCurrentAssets and totalCurrentLiabilities :
        quickRatio = (totalCurrentAssets - inventory) / totalCurrentLiabilities
    else: 
        quickRatio = None 

    symbol_data = {
        "Ticker" : symbol,
        "totalEquity" : totalEquity,
        "totalLiabilties" : totalLiabilties,
        "totalAssets" :totalAssets,
        "totalCurrentAssets" : totalCurrentAssets,
        "totalCurrentLiabilities" : totalCurrentLiabilities,
        "inventory" : inventory,
        "Debt to  Equit Ratio " : dbRatio,
        "Current Ratio": currentRatio,
        "Quick Ration" : quickRatio,
        "Trailing PE" : symbolInfo.get('trailingPE'),
        "PEG Ratio" : symbolInfo.get('pegRatio'),
        "EV/EBITA": symbolInfo.get('enterprisetoEbita'),
        "ROE": symbolInfo.get('returnOnEquity')
    }

    symbolData.append(symbol_data)


for stock in symbolData:
    print("\nStock Information")
    for key, value in stock.items():
        print(f'{key}: {value}')
