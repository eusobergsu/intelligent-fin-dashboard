# app/models/market_models.py
from pydantic import BaseModel
from typing import List, Dict

class OHLC(BaseModel):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int

class StockHistoryResponse(BaseModel):
    symbol: str
    history: List[OHLC]

class MarketSummaryResponse(BaseModel):
    source: str
    timestamp: str
    indices: Dict[str, float]
    market_sentiment: str
