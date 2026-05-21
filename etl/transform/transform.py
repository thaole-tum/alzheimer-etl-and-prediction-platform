import pandas as pd


class Transform:
    def clean_data(self, df):
        print("Cleaning data...")
        return df.dropna().copy()

    def feature_engineering(self, df):
        print("Creating features...")

        result = df.copy()

        if "MMSE" in result.columns:
            result["cognitive_score"] = pd.to_numeric(result["MMSE"], errors="coerce")
        elif "cognitive_score" not in result.columns:
            raise KeyError("Expected either 'MMSE' or 'cognitive_score' in the input data.")

        required_columns = ["MemoryComplaints", "BehavioralProblems", "CholesterolHDL"]
        missing = [column for column in required_columns if column not in result.columns]
        if missing:
            raise KeyError(f"Missing required columns for feature engineering: {', '.join(missing)}")

        result["risk_score"] = (
            0.5 * pd.to_numeric(result["MemoryComplaints"], errors="coerce")
            + 0.3 * pd.to_numeric(result["BehavioralProblems"], errors="coerce")
            + 0.2 * pd.to_numeric(result["CholesterolHDL"], errors="coerce")
        )

        result["age"] = pd.to_numeric(result["Age"], errors="coerce")
        result["gender"] = pd.to_numeric(result["Gender"], errors="coerce")
        result["bmi"] = pd.to_numeric(result["BMI"], errors="coerce")

        return result

    def run(self, df):
        cleaned = self.clean_data(df)
        return self.feature_engineering(cleaned)
