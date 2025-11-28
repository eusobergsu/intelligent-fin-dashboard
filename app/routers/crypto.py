from fastapi import APIRouter
from datetime import datetime

router = APIRouter(prefix="/crypto", tags=["crypto"])

@router.get("/summary")
def crypto_summary():
    return {
        "data": [
            {"symbol": "BTC", "price": 68000, "change": +2.5},
            {"symbol": "ETH", "price": 3500, "change": +1.8},
            {"symbol": "SOL", "price": 148, "change": -0.9},
        ],
        "timestamp": datetime.utcnow().isoformat(),
    }

@router.get("/ticker/{symbol}")
def crypto_ticker(symbol: str, interval: str = "1h"):
    return {
        "symbol": symbol.upper(),
        "interval": interval,
        "prices": [
            {"t": i, "value": 50000 + i * 10} for i in range(5)
        ]
    }
