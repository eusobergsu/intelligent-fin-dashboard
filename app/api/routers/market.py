from fastapi import APIRouter
from datetime import datetime, timedelta

router = APIRouter(prefix="/market", tags=["market"])

# Mock summary for a list of tickers
@router.get("/summary")
def market_summary():
    return {
        "source": "mock",
        "timestamp": datetime.utcnow().isoformat(),
        "data": [
            {"ticker": "AAPL", "price": 178.23, "change_24h": -0.8, "volume": 12_345_678},
            {"ticker": "MSFT", "price": 412.50, "change_24h": 0.6, "volume": 8_765_432},
            {"ticker": "PETR4.SA", "price": 26.10, "change_24h": 1.2, "volume": 3_210_987}
        ]
    }

# Mock OHLC history for a single ticker
@router.get("/history/{ticker}")
def market_history(ticker: str, days: int = 7):
    base = datetime.utcnow()
    history = []
    for i in range(days):
        dt = (base - timedelta(days=i)).date().isoformat()
        history.append({
            "date": dt,
            "open": round(100 + i * 0.5, 2),
            "high": round(101 + i * 0.6, 2),
            "low": round(99 + i * 0.4, 2),
            "close": round(100 + i * 0.5, 2),
            "volume": 100000 + i * 1000
        })
    return {"ticker": ticker.upper(), "history": history[::-1]}
