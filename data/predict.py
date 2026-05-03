import pandas as pd
import joblib

class Predictor:
    def __init__(self):
        self.model = joblib.load("model.pkl")

    def predict(self, input_data: dict):
        df = pd.DataFrame([input_data])

        X= df.drop(columns=['Diagnosis', 'DoctorInCharge'])

        prediction = self.model.predict(X)[0]
        return float(prediction)