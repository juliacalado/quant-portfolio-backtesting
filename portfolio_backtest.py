import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# assets in the portfolio
tickers = ["SPY", "TLT", "GLD"]

# download historical data
data = yf.download(tickers, start="2015-01-01")["Adj Close"]

# compute daily returns
returns = data.pct_change().dropna()

# portfolio weights
weights = np.array([0.5, 0.3, 0.2])

# compute portfolio returns
portfolio_returns = returns.dot(weights)

# annualized return
annual_return = np.mean(portfolio_returns) * 252

# annualized volatility
volatility = np.std(portfolio_returns) * np.sqrt(252)

# sharpe ratio
sharpe_ratio = annual_return / volatility

print("Annual Return:", annual_return)
print("Volatility:", volatility)
print("Sharpe Ratio:", sharpe_ratio)

# cumulative performance
cumulative_returns = (1 + portfolio_returns).cumprod()

# plot portfolio performance
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

