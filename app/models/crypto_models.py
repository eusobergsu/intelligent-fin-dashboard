# app/models/crypto_models.py
from pydantic import BaseModel
from typing import List, Dict

class Tick(BaseModel):
    timestamp: str
    price: float
    volume: int

class CryptoTickerResponse(BaseModel):
    ticker: str
    interval: str
    ticks: List[Tick]

class CryptoSummaryResponse(BaseModel):
    source: str
    timestamp: str
    data: List[Dict]
