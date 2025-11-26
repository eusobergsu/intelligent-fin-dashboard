from fastapi import FastAPI

app = FastAPI(title="Intelligent Financial Dashboard API")

@app.get("/health")
def health_check():
    return {"status": "ok"}
