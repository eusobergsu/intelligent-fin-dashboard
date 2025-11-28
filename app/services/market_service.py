from datetime import datetime, timedelta
import random

def get_market_summary():
    return {
        "indices": {
            "SP500": 5134.50,
            "NASDAQ": 16234.10,
            "DOWJONES": 38921.20,
        },
        "sentiment": "bullish",
        "timestamp": datetime.utcnow().isoformat()
    }

def get_stock_history(symbol: str, days: int = 5):
    """
    Retorna histórico fictício para os últimos X dias.
    O teste espera:
    {
        "symbol": "AAPL",
        "history": [ { "date": "...", "close": 123.45 }, ... ]
    }
    """

    today = datetime.utcnow()

    history = []
    for i in range(days):
        day = today - timedelta(days=i)
        history.append({
            "date": day.strftime("%Y-%m-%d"),
            "close": round(random.uniform(100, 300), 2)
        })

    # inverter para ficar ordem cronológica
    history.reverse()

    return {
        "symbol": symbol,
        "history": history
    }
