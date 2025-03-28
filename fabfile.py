from fabric import task

@task
def run_fastapi(c):
    """Start the FastAPI server with reload enabled."""
    c.run("uvicorn src.peak_mentions.api.main:app --reload")

@task
def ingest_all(c):
    """Run the dlt ingestion pipeline."""
    c.run("python src/peak_mentions/connectors/dlt_pipeline.py")

@task
def duckdb_ui(c):
    """Open DuckDB in the browser."""
    c.run("duckdb --ui mentions_pipeline.duckdb")