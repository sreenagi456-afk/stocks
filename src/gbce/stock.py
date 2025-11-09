"""
Stock Module for GBCE exchange
"""
from datetime import datetime, timedelta
from typing import List, Optional
from .enums import StockType, TradeIndicator
from .trade import Trade


class Stock:
    """Represents a stock in the GBCE exchange"""
   
    def __init__(self, symbol: str, stock_type: StockType, last_dividend: int,
                 fixed_dividend: Optional[float], par_value: int):
        """
        Initialize a stock
       
        Args:
            symbol: Stock symbol (e.g., 'TEA')
            stock_type: Common or Preferred
            last_dividend: Last dividend in pennies
            fixed_dividend: Fixed dividend as decimal (None for Common stocks)
            par_value: Par value in pennies
        """
        self.symbol = symbol
        self.type = stock_type
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value
        self.trades: List[Trade] = []
   
    def calculate_dividend_yield(self, price: float) -> float:
        """
        Calculate dividend yield for given price
       
        Args:
            price: Stock price in pennies
           
        Returns:
            Dividend yield as decimal
           
        Raises:
            ValueError: If price is not positive
        """
        if price <= 0:
            raise ValueError("Price must be positive")
       
        if self.type == StockType.COMMON:
            return self.last_dividend / price
        else:  # Preferred stock
            if self.fixed_dividend is None:
                raise ValueError("Preferred stock must have fixed dividend")
            return (self.fixed_dividend * self.par_value) / price
   
    def calculate_pe_ratio(self, price: float) -> Optional[float]:
        """
        Calculate P/E Ratio for given price
       
        Args:
            price: Stock price in pennies
           
        Returns:
            P/E Ratio or None if dividend is zero
        """
        dividend = (self.fixed_dividend * self.par_value if self.type == StockType.PREFERRED
                   else self.last_dividend)
       
        if dividend == 0:
            return None
       
        return price / dividend
   
    def record_trade(self, quantity: int, indicator: TradeIndicator, price: float) -> None:
        """
        Record a trade for this stock
       
        Args:
            quantity: Number of shares traded
            indicator: BUY or SELL
            price: Trade price in pennies
           
        Raises:
            ValueError: If quantity or price is not positive
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if price <= 0:
            raise ValueError("Price must be positive")
       
        trade = Trade(self.symbol, quantity, indicator, price)
        self.trades.append(trade)
   
    def calculate_volume_weighted_price(self, minutes: int = 5) -> float:
        """
        Calculate volume weighted stock price based on trades in past N minutes
       
        Args:
            minutes: Time window in minutes (default: 5)
           
        Returns:
            Volume weighted stock price in pennies
        """
        cutoff_time = datetime.now() - timedelta(minutes=minutes)
       
        recent_trades = [
            trade for trade in self.trades
            if trade.timestamp >= cutoff_time
        ]
       
        if not recent_trades:
            return 0.0
       
        total_value = sum(trade.price * trade.quantity for trade in recent_trades)
        total_quantity = sum(trade.quantity for trade in recent_trades)
       
        if total_quantity == 0:
            return 0.0
       
        return total_value / total_quantity
   
    def __repr__(self) -> str:
        return f"Stock(symbol='{self.symbol}', type={self.type.value}, last_dividend={self.last_dividend})" 
Displaying Homework Assignment - Super Simple Stocks - Candidate.pdf.
