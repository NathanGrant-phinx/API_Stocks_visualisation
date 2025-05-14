import yfinance as yf






sns.set(style="darkgrid")

stock_symbol = "AAPL"
stock = yf.Ticker(stock_symbol)
df = stock.history(period="6mo")
print(df.head())

df = df.reset_index["Date", "Open", "Close", "High","Low", "Volume"]
df["Date"] = df["Date"].astype(str)
print(df.head())