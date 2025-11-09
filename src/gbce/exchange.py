"""
Exchange module for GBCE
"""

import math
from typing import Dict, List
from .stock import Stock
from .enums import TradeIndicator


class StockExchange:
    """Main class representing the GBCE stock exchange"""
   
    def __init__(self):
        self.stocks: Dict[str, Stock] = {}
   
    def add_stock(self, stock: Stock) -> None:
        """
        Add a stock to the exchange
       
        Args:
            stock: Stock instance to add
        """
        self.stocks[stock.symbol] = stock
   
    def get_stock(self, symbol: str) -> Stock:
        """
        Get stock by symbol
       
        Args:
            symbol: Stock symbol
           
        Returns:
            Stock instance
           
        Raises:
            ValueError: If stock symbol not found
        """
        if symbol not in self.stocks:
            raise ValueError(f"Stock {symbol} not found")
        return self.stocks[symbol]
   
    def record_trade(self, symbol: str, quantity: int, indicator: TradeIndicator, price: float) -> None:
        """
        Record a trade for a stock
       
        Args:
            symbol: Stock symbol
            quantity: Number of shares
            indicator: BUY or SELL
            price: Trade price in pennies
        """
        stock = self.get_stock(symbol)
        stock.record_trade(quantity, indicator, price)
   
    def calculate_all_share_index(self) -> float:
        """
        Calculate GBCE All Share Index using geometric mean of Volume Weighted Stock Prices
       
        Returns:
            Geometric mean of all volume weighted stock prices
        """
        volume_weighted_prices = [
            stock.calculate_volume_weighted_price()
            for stock in self.stocks.values()
        ]
       
        # Filter out zero prices (stocks with no recent trades)
        non_zero_prices = [price for price in volume_weighted_prices if price > 0]
       
        if not non_zero_prices:
            return 0.0
       
        # Calculate geometric mean: (P1 * P2 * ... * Pn)^(1/n)
        product = math.prod(non_zero_prices)
        return product ** (1 / len(non_zero_prices))
   
    def get_all_stocks(self) -> List[Stock]:
        """
        Get all stocks in the exchange
       
        Returns:
            List of all Stock instances
        """
        return list(self.stocks.values())


def create_sample_exchange() -> StockExchange:
    """
    Create and populate exchange with sample data from requirements
   
    Returns:
        StockExchange instance with sample data
    """
    from .enums import StockType
   
    exchange = StockExchange()
   
    # Add sample stocks from the requirements
    exchange.add_stock(Stock("TEA", StockType.COMMON, 0, None, 100))
    exchange.add_stock(Stock("POP", StockType.COMMON, 8, None, 100))
    exchange.add_stock(Stock("ALE", StockType.COMMON, 23, None, 60))
    exchange.add_stock(Stock("GIN", StockType.PREFERRED, 8, 0.02, 100))
    exchange.add_stock(Stock("JOE", StockType.COMMON, 13, None, 250))
   
    return exchange 
Displaying Homework Assignment - Super Simple Stocks - Candidate.pdf.
