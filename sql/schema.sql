CREATE TABLE IF NOT EXISTS alzheimer_data (
    id SERIAL PRIMARY KEY,
    age INTEGER NOT NULL,
    gender INTEGER NOT NULL,
    bmi DOUBLE PRECISION NOT NULL,
    cognitive_score DOUBLE PRECISION NOT NULL,
    risk_score DOUBLE PRECISION NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_alzheimer_data_risk_score
    ON alzheimer_data (risk_score DESC);

ALTER TABLE IF EXISTS alzheimer_data
    ADD COLUMN IF NOT EXISTS cognitive_score DOUBLE PRECISION;
