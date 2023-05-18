from fastapi import FastAPI
from src.routes import user, registry, receipt, client

app = FastAPI()
app.include_router(user.api_router)
app.include_router(registry.api_router)
app.include_router(receipt.api_router)
app.include_router(client.api_router)
