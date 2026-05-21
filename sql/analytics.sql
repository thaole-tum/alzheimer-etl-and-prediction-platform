SELECT
    gender,
    COUNT(*) AS patient_count,
    AVG(risk_score) AS avg_risk_score
FROM alzheimer_data
GROUP BY gender
ORDER BY avg_risk_score DESC;

SELECT
    age,
    gender,
    bmi,
    cognitive_score,
    risk_score
FROM alzheimer_data
ORDER BY risk_score DESC
LIMIT 10;

SELECT
    CASE
        WHEN age < 60 THEN 'Under 60'
        WHEN age BETWEEN 60 AND 69 THEN '60-69'
        WHEN age BETWEEN 70 AND 79 THEN '70-79'
        ELSE '80+'
    END AS age_band,
    COUNT(*) AS patient_count,
    AVG(risk_score) AS avg_risk_score
FROM alzheimer_data
GROUP BY age_band
ORDER BY age_band;
