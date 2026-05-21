# Alzheimer Data ETL and Prediction Pipeline

An end-to-end data project focused on three practical skills that are valuable in data engineering and applied machine learning:

- Building an ETL pipeline for structured healthcare data
- Running PostgreSQL with Docker for a reproducible local environment
- Training and using a machine-learning model to support Alzheimer disease prediction

This repository is designed to show how raw data can be extracted, cleaned, transformed, loaded into a database, and then used for downstream analytics or prediction.

## Project Highlights

- ETL pipeline built in Python with a clear `extract -> transform -> load` structure
- PostgreSQL containerized with Docker Compose for easy local setup
- Feature engineering for Alzheimer-related risk analysis
- Machine-learning prediction workflow using a serialized model artifact
- SQL scripts for database schema and analytics queries
- Basic test coverage for the transformation and prediction layers

## Repository Structure

```text
.
|-- data/
|   |-- raw/                 # Raw input dataset and preprocessing notebook
|   |-- processed/           # Cleaned output data
|   |-- model.pkl            # Trained prediction model
|   `-- predict.py           # Inference helper
|-- tests/
|   |-- test_predict.py
|   `-- test_transform.py
|-- docker/
|   `-- Dockerfile
|-- etl/
|   |-- extract/             # CSV extraction logic
|   |-- transform/           # Cleaning and feature engineering
|   |-- load/                # PostgreSQL loading logic
|   `-- pipeline.py          # Orchestrates the ETL flow
|-- sql/
|   |-- schema.sql           # Table definition
|   `-- analytics.sql        # Example analytics queries
|-- requirements.txt
|-- .env.example
`-- docker-compose.yml       # PostgreSQL container setup
```

## ETL Pipeline

The pipeline follows a simple and readable structure:

1. `Extract`
   - Reads the Alzheimer dataset from CSV
2. `Transform`
   - Removes missing values
   - Creates `cognitive_score` from `MMSE`
   - Creates `risk_score` from complaint and cholesterol features
3. `Load`
   - Inserts standardized records into PostgreSQL

The main orchestration entry point is `etl/pipeline.py`.

## Machine Learning Prediction

The repository also includes a lightweight prediction workflow in `data/predict.py`.

- A trained model is stored as `data/model.pkl`
- Input data is converted into a `pandas` DataFrame
- Irrelevant columns are removed before inference
- The model returns a prediction for the given sample

This makes the project feel complete: it is not only about moving data, but also about using data for a prediction task.

## Docker and PostgreSQL

The project uses Docker Compose to launch PostgreSQL locally.

- PostgreSQL runs in a container
- A Python app service runs the ETL pipeline against the database
- Data is persisted in a Docker volume
- The setup is simple enough to reproduce on a new machine

This is useful for showing practical Docker basics in a job application.

### Docker Compose Services

- `postgres`: PostgreSQL 15 database
- `app`: Python container that runs the ETL pipeline

## Database Schema

The database schema is defined in `sql/schema.sql`.

The table stores fields related to Alzheimer data analysis, including:

- Age
- Gender
- BMI
- Cognitive score
- Risk score

## Tech Stack

- Python
- pandas
- PostgreSQL
- psycopg2
- Docker
- Docker Compose
- SQL
- a serialized machine-learning model workflow
- pytest

## How to Run

### 1. Configure environment variables

```bash
copy .env.example .env
```

### 2. Start the full stack

```bash
docker compose up --build
```

If you want to run only the database locally, you can still start just `postgres` with `docker compose up -d postgres`.

### 3. Run the ETL pipeline directly

```bash
python etl/pipeline.py
```

### 4. Run prediction code

```bash
python data/predict.py
```

### 5. Run tests

```bash
pytest
```

## Example Use Cases

- Load Alzheimer dataset records into a relational database
- Create a simple risk score feature for analysis
- Run SQL queries against the loaded data
- Use the saved model to generate predictions from structured input

## Data Source

The analysis and modeling in this project use the public Alzheimer’s Disease Dataset from Kaggle:
[Alzheimer’s Disease Dataset](https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset)

## Next Improvements

If you want to make the project even stronger for interviews, the next best upgrades would be:

- Add logging and validation checks
- Expose the prediction workflow through a small API or CLI
- Add a short architecture diagram to the README
