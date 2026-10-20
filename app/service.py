import json
import pathlib
from catboost import CatBoostClassifier
from .schemas import ScoringRequest, ScoringResponse
from .preprocessing import preprocessing

class ScoringService:
    def __init__(self):
        BASE_DIR = pathlib.Path(__file__).resolve().parent
        CONFIG_PATH = BASE_DIR / "artifacts" / "config.json"
        MODEL_PATH = BASE_DIR / "artifacts" / "model.cbm"
        with open(CONFIG_PATH, "r") as js:
            self._config = json.load(js)
        self.model = CatBoostClassifier()
        self.model.load_model(MODEL_PATH)

    def predict(self, payload: ScoringRequest) -> ScoringResponse:

        request = payload.model_dump(by_alias=True)

        request = preprocessing(request)
        
        feats = [request[x] for x in self._config["features"]]

        prob = self.model.predict_proba([feats])[0][1]
        return ScoringResponse(default_probability = prob, is_approved=prob < self._config["threshold"])