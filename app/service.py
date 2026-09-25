import json
import pathlib
from catboost import CatBoostClassifier
from schemas import ScoringRequest, ScoringResponse

class ScoringService:
    def __init__(self):
        BASE_DIR = pathlib.Path(__file__).resolve().parent
        CONFIG_PATH = BASE_DIR / "artifacts" / "config.json"
        MODEL_PATH = BASE_DIR / "artifacts" / "model.cbm"
        with open(CONFIG_PATH, "r") as js:
            config = json.load(js)
        self.model = CatBoostClassifier()
        self.model.load_model(MODEL_PATH)

    def predict(self, payload: ScoringRequest) -> ScoringResponse:
        payload.model_dump(by_alias=True)

