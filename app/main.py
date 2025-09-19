from fastapi import FastAPI
from .api.endpoints import router

app = FastAPI(
    title="Proceder Brain API",
    description="PDF RAG Pipeline for intelligent document analysis",
    version="1.0.0"
)

app.include_router(router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Proceder Brain API is running"}
