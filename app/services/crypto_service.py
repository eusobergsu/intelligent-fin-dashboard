# app/services/crypto_service.py
from datetime import datetime, timedelta
from typing import List, Dict

def get_crypto_summary() -> Dict:
    """
    Return a mock crypto market summary.
    """
    return {
        "source": "mock_service",
        "timestamp": datetime.utcnow().isoformat(),
        "data": [
            {"ticker": "BTC", "price": 42000.12, "change_24h": 2.3, "market_cap": 800_000_000_000},
            {"ticker": "ETH", "price": 2800.45, "change_24h": -1.1, "market_cap": 330_000_000_000},
            {"ticker": "SOL", "price": 60.10, "change_24h": 4.5, "market_cap": 20_000_000_000}
        ]
    }

def get_crypto_ticker(symbol: str, interval: str = "1h") -> Dict:
    """
    Return a mock time-series for a crypto ticker.
    """
    base = datetime.utcnow()
    ticks: List[Dict] = []
    for i in range(12):
        ticks.append({
            "timestamp": (base - timedelta(hours=i)).isoformat(),
            "price": round(1000 + i * 2.5, 2),
            "volume": 1000 + i * 10
        })
    return {"ticker": symbol.upper(), "interval": interval, "ticks": ticks[::-1]}
