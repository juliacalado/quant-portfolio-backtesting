import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tickers = ["SPY", "TLT", "GLD"]

data = yf.download(tickers, start="2015-01-01")["Adj Close"]

returns = data.pct_change().dropna()

weights = np.array([0.5, 0.3, 0.2])

portfolio_returns = returns.dot(weights)

mean_return = np.mean(portfolio_returns) * 252
volatility = np.std(portfolio_returns) * np.sqrt(252)

sharpe = mean_return / volatility

print("Annual Return:", mean_return)
print("Volatility:", volatility)
print("Sharpe Ratio:", sharpe)

cumulative_returns = (1 + portfolio_returns).cumprod()

plt.plot(cumulative_returns)
plt.title("Portfolio Performance")
plt.show()
