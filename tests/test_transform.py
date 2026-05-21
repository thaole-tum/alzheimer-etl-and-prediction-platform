import pandas as pd

from etl.transform.transform import Transform


def test_transform_creates_standardized_columns():
    df = pd.DataFrame(
        [
            {
                "Age": 72,
                "Gender": 1,
                "BMI": 24.5,
                "MMSE": 21.0,
                "MemoryComplaints": 1,
                "BehavioralProblems": 0,
                "CholesterolHDL": 35.0,
            }
        ]
    )

    transformed = Transform().run(df)

    assert transformed.loc[0, "age"] == 72
    assert transformed.loc[0, "gender"] == 1
    assert transformed.loc[0, "bmi"] == 24.5
    assert transformed.loc[0, "cognitive_score"] == 21.0
    assert transformed.loc[0, "risk_score"] == 0.5 * 1 + 0.3 * 0 + 0.2 * 35.0
