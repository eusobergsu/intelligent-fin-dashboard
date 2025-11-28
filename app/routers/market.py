from fastapi import APIRouter
from app.services.market_service import get_market_summary

router = APIRouter(prefix="/market", tags=["market"])

@router.get("/summary")
def market_summary():
    summary = get_market_summary()

    # Converter índices dict -> lista
    data_list = [
        {"name": name, "value": value}
        for name, value in summary["indices"].items()
    ]

    return {
        "data": data_list,
        "sentiment": summary["sentiment"],
        "timestamp": summary["timestamp"],
    }
