from fastapi import FastAPI
from contextlib import asynccontextmanager
from .schemas import ScoringRequest, ScoringResponse
from .service import ScoringService
from .schemas import Health
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.service = ScoringService()
    yield

app = FastAPI(title="Scoring Service", lifespan=lifespan)


@app.get("/health")
async def check_health() -> Health:
    return {"status": "ok"}

@app.post("/predict")
def predict_probability(payload: ScoringRequest) -> ScoringResponse:
    service = app.state.service
    return service.predict(payload)

