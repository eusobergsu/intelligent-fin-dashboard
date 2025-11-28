from fastapi import APIRouter
from app.services.crypto_service import get_crypto_summary, get_crypto_ticker

router = APIRouter(prefix="/crypto", tags=["crypto"])

@router.get("/summary")
def crypto_summary():
    return get_crypto_summary()

@router.get("/ticker/{symbol}")
def crypto_ticker(symbol: str, interval: str = "1h"):
    return get_crypto_ticker(symbol, interval)
