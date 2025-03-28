from fabric import task
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

@task
def run_fastapi(c):
    c.run(f"cd {BASE_DIR} && uvicorn src.peak_mentions.api.main:app --reload")

@task
def ingest_all(c):
    c.run(f"cd {BASE_DIR} && python src/peak_mentions/connectors/dlt_pipeline.py")

@task
def duckdb_ui(c):
    c.run(f"cd {BASE_DIR} && duckdb --ui mentions_pipeline.duckdb")

@task
def dbt_build(c):
    c.run(f"cd {BASE_DIR} && DBT_PROFILES_DIR=dbt_project dbt build --project-dir dbt_project")

@task
def generate_docs(c):
    """Generate DBT docs."""
    c.run(f"cd {BASE_DIR} && dbt docs generate --project-dir dbt_project --profiles-dir dbt_project --profile peak_mentions")

@task
def serve_docs(c):
    """Serve DBT docs locally."""
    c.run(f"cd {BASE_DIR} && dbt docs serve --project-dir dbt_project --profiles-dir dbt_project --profile peak_mentions")