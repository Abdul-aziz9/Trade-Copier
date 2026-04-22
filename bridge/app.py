from fastapi import FastAPI

from db import init_db
from routes.health import router as health_router
from routes.ingest import router as ingest_router

app = FastAPI(title="Trade Copier Bridge", version="0.1.0")


@app.on_event("startup")
def startup_event() -> None:
    init_db()


app.include_router(health_router)
app.include_router(ingest_router)