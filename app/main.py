from fastapi import FastAPI
from app.api.routers import market_router, crypto_router
from app.core.config import settings
from app.routers import market, crypto

app = FastAPI(title=settings.app_name)

# Register routers
app.include_router(market_router)
app.include_router(crypto_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
