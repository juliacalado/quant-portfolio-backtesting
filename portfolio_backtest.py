import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tickers = ["SPY", "TLT", "GLD"]

data = yf.download(tickers, start="2015-01-01")["Close"]
returns = data.pct_change().dropna()
weights = np.array([0.5, 0.3, 0.2])
portfolio_returns = returns.dot(weights)
annual_return = np.mean(portfolio_returns) * 252
volatility = np.std(portfolio_returns) * np.sqrt(252)
sharpe_ratio = annual_return / volatility

print("Annual Return:", annual_return)
print("Volatility:", volatility)
print("Sharpe Ratio:", sharpe_ratio)

cumulative_returns = (1 + portfolio_returns).cumprod()

plt.figure(figsize=(10,5))
plt.plot(cumulative_returns)
plt.title("Portfolio Performance")
plt.xlabel("Date")
plt.ylabel("Cumulative Returns")
plt.show()

# maximum drawdown
rolling_max = cumulative_returns.cummax()
drawdown = cumulative_returns / rolling_max - 1

max_drawdown = drawdown.min()

print("Maximum Drawdown:", max_drawdown)

