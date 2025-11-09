# Super Simple Stocks - GBCE

A Python implementation of the Global Beverage Corporation Exchange stock trading system.

## Features

- Calculate dividend yield for Common and Preferred stocks
- Calculate P/E Ratio
- Record trades with timestamps
- Calculate Volume Weighted Stock Price
- Calculate GBCE All Share Index using geometric mean

## Installation

```bash
pip install -e .

## Execution
"""
from gbce import StockExchange, Stock, StockType, TradeIndicator

# Create exchange with sample data
exchange = StockExchange.create_sample_exchange()

# Get a stock
tea = exchange.get_stock("TEA")

# Calculate dividend yield
dividend_yield = tea.calculate_dividend_yield(100)

# Record a trade
exchange.record_trade("TEA", 100, TradeIndicator.BUY, 105)

# Calculate All Share Index
index = exchange.calculate_all_share_index()

"""
