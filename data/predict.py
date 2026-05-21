from pathlib import Path

import joblib
import pandas as pd


MODEL_PATH = Path(__file__).resolve().with_name("model.pkl")


class Predictor:
    def __init__(self, model_path=MODEL_PATH):
        self.model_path = Path(model_path)
        if not self.model_path.exists():
            raise FileNotFoundError(f"Model file not found: {self.model_path}")

        self.model = joblib.load(self.model_path)
        self.feature_names = getattr(self.model, "feature_names_in_", None)

    def _prepare_features(self, input_data: dict):
        df = pd.DataFrame([input_data])

        if self.feature_names is not None:
            if "RiskScore" in self.feature_names and "RiskScore" not in df.columns:
                if "risk_score" in df.columns:
                    df["RiskScore"] = df["risk_score"]
                elif {"MemoryComplaints", "BehavioralProblems", "CholesterolHDL"}.issubset(df.columns):
                    df["RiskScore"] = (
                        0.5 * pd.to_numeric(df["MemoryComplaints"], errors="coerce")
                        + 0.3 * pd.to_numeric(df["BehavioralProblems"], errors="coerce")
                        + 0.2 * pd.to_numeric(df["CholesterolHDL"], errors="coerce")
                    )

            missing = [column for column in self.feature_names if column not in df.columns]
            if missing:
                raise KeyError(f"Missing input columns for prediction: {', '.join(missing)}")
            return df.loc[:, self.feature_names]

        drop_columns = [column for column in ["Diagnosis", "DoctorInCharge"] if column in df.columns]
        return df.drop(columns=drop_columns)

    def predict(self, input_data: dict):
        features = self._prepare_features(input_data)
        prediction = self.model.predict(features)[0]
        return prediction.item() if hasattr(prediction, "item") else prediction


if __name__ == "__main__":
    sample_path = Path(__file__).resolve().parents[1] / "data" / "raw" / "alzheimers_disease_data.csv"
    sample_row = pd.read_csv(sample_path).drop(columns=["Diagnosis", "DoctorInCharge"]).iloc[0].to_dict()

    predictor = Predictor()
    print(f"Sample prediction: {predictor.predict(sample_row)}")
