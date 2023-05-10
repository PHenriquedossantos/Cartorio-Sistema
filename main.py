from fastapi import FastAPI
from src.routes import user, cartorio, recibo

app = FastAPI()
app.include_router(user.api_router)
app.include_router(cartorio.api_router)
app.include_router(recibo.api_router)