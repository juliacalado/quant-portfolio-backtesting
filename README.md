# Portfolio Backtesting in Python

A simple Python project to simulate a multi-asset portfolio and analyze its performance using historical market data.

## Portfolio

We track three assets:

- **SPY** – US Stocks (S&P 500 ETF)  
- **TLT** – US Treasury Bonds  
- **GLD** – Gold  

## What it does

- Downloads historical price data using `yfinance`  
- Calculates daily returns and portfolio performance  
- Computes key metrics:  
  - Annual return  
  - Volatility  
  - Sharpe ratio  
  - Maximum drawdown  
- Compares the portfolio with the S&P 500  
- Plots cumulative returns and drawdowns  

## Tools

- Python  
- pandas, NumPy  
- matplotlib  
- yfinance  

## Why it’s useful

This project is a simple example of how you can test investment ideas, analyze risk, and compare performance with the market. 
