import glob
from pathlib import Path
from typing import Any

import joblib
import numpy as np

MODELS_DIR = Path(__file__).parent


SUPPORTED_ANIMALS: set[str] = {
    Path(p).stem.replace("_model", "")
    for p in glob.glob(str(MODELS_DIR / "*_model.joblib"))
}


_cache: dict[str, Any] = {}


def load_model(animal: str) -> Any:
    """Load and cache the sklearn Pipeline for the given animal.

    Each .joblib file is a fitted sklearn Pipeline whose steps include
    a TfidfVectorizer followed by an SVC classifier.
    """
    animal = animal.lower().strip()

    if animal not in SUPPORTED_ANIMALS:
        raise ValueError(
            f"No model found for animal '{animal}'. "
            f"Supported animals: {sorted(SUPPORTED_ANIMALS)}"
        )

    if animal not in _cache:
        model_path = MODELS_DIR / f"{animal}_model.joblib"
        pipeline = joblib.load(model_path)

        if not hasattr(pipeline, "predict"):
            raise RuntimeError(
                f"Model file for '{animal}' does not expose a predict() method "
                f"(got {type(pipeline).__name__})"
            )

        _cache[animal] = pipeline

    return _cache[animal]


def predict(animal: str, description: str) -> dict[str, Any]:

    pipeline = load_model(animal)

    tfidf = pipeline.named_steps["tfidf"]

    input_vector = tfidf.transform([description])

   
    if input_vector.nnz < 2:
        return {
            "prediction": " ",
            "probabilities": {}
        }

    prediction: str = pipeline.predict([description])[0]

    probabilities: dict[str, float] = {}

    if hasattr(pipeline, "predict_proba"):
        proba_values: np.ndarray = pipeline.predict_proba([description])[0]

        probabilities = {
            str(cls): round(float(prob), 6)
            for cls, prob in zip(pipeline.classes_, proba_values)
        }

    return {
        "prediction": str(prediction),
        "probabilities": probabilities,
    }
