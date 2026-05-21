from data.predict import Predictor


class FakeModel:
    feature_names_in_ = ["Age", "Gender", "BMI"]

    def predict(self, features):
        assert list(features.columns) == ["Age", "Gender", "BMI"]
        return [1]


def test_predictor_uses_model_feature_names(monkeypatch, tmp_path):
    model_path = tmp_path / "model.pkl"
    model_path.write_bytes(b"placeholder")

    monkeypatch.setattr("data.predict.joblib.load", lambda _: FakeModel())

    predictor = Predictor(model_path=model_path)
    prediction = predictor.predict({"Age": 70, "Gender": 1, "BMI": 23.1, "Diagnosis": 0})

    assert prediction == 1
