from fastapi import FastAPI
from app.api.routers import market_router, crypto_router
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME)

# Register routers
app.include_router(market_router)
app.include_router(crypto_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
