from fastapi import FastAPI
from app.api import compte

app = FastAPI(title="API Gestion Portefeuille Bancaire")

app.include_router(compte.router, prefix="/api", tags=["Comptes"])