import yfinance as yf
import matplotlib.pyplot as plt

#Download historical  data of STOCK.NS
ticker = input("Enter Stock Name: ")
date = yf.download(ticker,start = "2021-01-01", end = "2023-10-17")

#Plot the stock chart
plt.figure(figsize=(10,5))
plt.plot(date["Close"])
plt.title(f"{ticker} Stock Chart")
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.show()



