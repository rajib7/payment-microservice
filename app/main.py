from fastapi import FastAPI, Request
from .db import init_db
from .api.payments import router as payments_router

app = FastAPI(title="Payment Microservice", version="0.1.0")

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(payments_router)

@app.post("/webhooks")
async def webhook(request: Request):
    payload = await request.json()
    return {"received": True, "event": payload}
