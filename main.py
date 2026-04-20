from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator

from model_loader import SUPPORTED_ANIMALS, predict
from treatments import get_treatment
from attention import get_attention
import asyncio

CONFIDENCE_THRESHOLD = 0.7
LOW_CONFIDENCE_MESSAGE = "Please consult a veterinarian if the problem persists."

app = FastAPI(
    title="Animal Disease Detection API",
    description="Detects diseases from a text description of observations about an animal.",
    version="1.0.0",
)


class PredictRequest(BaseModel):
    animal: str
    description: str

    @field_validator("animal")
    @classmethod
    def animal_must_be_supported(cls, value: str) -> str:
        normalised = value.lower().strip()
        if normalised not in SUPPORTED_ANIMALS:
            raise ValueError(
                f"Unsupported animal '{value}'. "
                f"Supported animals: {sorted(SUPPORTED_ANIMALS)}"
            )
        return normalised

    @field_validator("description")
    @classmethod
    def description_must_not_be_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("description must not be empty")
        return value.strip()


class PredictResponse(BaseModel):
    animal: str
    prediction: str
    probabilities: dict[str, float]
    treatment: str
    attention: str


@app.post("/predict", response_model=PredictResponse)
async def predict_disease(request: PredictRequest) -> PredictResponse:
    """
    Given an animal type and a free-text observation, returns the most likely
    disease and the probability distribution over all known classes.
    """
    try:
        result = predict(request.animal, request.description)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Prediction error: {exc}") from exc

    top_confidence = max(result["probabilities"].values(), default=0.0)
    if top_confidence >= CONFIDENCE_THRESHOLD:
        treatment = get_treatment(request.animal, result["prediction"])
        attention = get_attention(request.animal, result["prediction"])
    else:
        treatment = LOW_CONFIDENCE_MESSAGE
        attention = ""

    await asyncio.sleep(2)
    return PredictResponse(
        animal=request.animal,
        prediction=result["prediction"],
        probabilities=result["probabilities"],
        treatment=treatment,
        attention=attention
    )
