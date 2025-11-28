from app.services.market_service import get_market_summary, get_stock_history
from app.services.crypto_service import get_crypto_summary, get_crypto_ticker

def test_market_summary():
    s = get_market_summary()
    assert "indices" in s

def test_stock_history():
    h = get_stock_history("AAPL", days=3)
    assert h["symbol"] == "AAPL"
    assert len(h["history"]) == 3

def test_crypto_summary():
    s = get_crypto_summary()
    assert "data" in s

def test_crypto_ticker():
    t = get_crypto_ticker("BTC", interval="1h")
    assert t["ticker"] == "BTC"
    assert "ticks" in t
