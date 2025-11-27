from fastapi import APIRouter
from datetime import datetime, timedelta

router = APIRouter(prefix="/crypto", tags=["crypto"])

@router.get("/summary")
def crypto_summary():
    return {
        "source": "mock",
        "timestamp": datetime.utcnow().isoformat(),
        "data": [
            {"ticker": "BTC", "price": 42000.12, "change_24h": 2.3, "market_cap": 800_000_000_000},
            {"ticker": "ETH", "price": 2800.45, "change_24h": -1.1, "market_cap": 330_000_000_000},
            {"ticker": "SOL", "price": 60.10, "change_24h": 4.5, "market_cap": 20_000_000_000}
        ]
    }

@router.get("/ticker/{ticker}")
def crypto_ticker(ticker: str, interval: str = "1h"):
    # Mock time-series ticks (simple)
    base = datetime.utcnow()
    ticks = []
    for i in range(12):
        ticks.append({
            "timestamp": (base - timedelta(hours=i)).isoformat(),
            "price": round(1000 + i * 2.5, 2),
            "volume": 1000 + i * 10
        })
    return {"ticker": ticker.upper(), "interval": interval, "ticks": ticks[::-1]}
