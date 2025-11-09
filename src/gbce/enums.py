"""
Enums for the GBCE stock exchange system
"""
from enum import Enum

class TradeIndicator(Enum):
    """Enum for buy/sell indicators"""
    BUY = "BUY"
    SELL = "SELL"


class StockType(Enum):
    """Enum for stock types"""
    COMMON = "Common"
    PREFERRED = "Preferred"
