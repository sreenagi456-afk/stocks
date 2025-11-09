"""
Trade module for GBCE
"""
from datetime import datetime
from .enums import TradeIndicator

class Trade:
    """Represents a single stock trade"""
   
    def __init__(self, stock_symbol: str, quantity: int, indicator: TradeIndicator, price: float):
        """
        Initialize a trade
       
        Args:
            stock_symbol: Symbol of the stock being traded
            quantity: Number of shares traded
            indicator: BUY or SELL indicator
            price: Trade price in pennies
        """
        self.stock_symbol = stock_symbol
        self.quantity = quantity
        self.indicator = indicator
        self.price = price
        self.timestamp = datetime.now()
   
    def __repr__(self) -> str:
        return (f"Trade(stock='{self.stock_symbol}', quantity={self.quantity}, "
                f"indicator={self.indicator.value}, price={self.price})") 
Displaying Homework Assignment - Super Simple Stocks - Candidate.pdf.
