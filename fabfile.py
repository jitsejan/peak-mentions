from fabric import task

@task
def run_fastapi(c):
    """Start the FastAPI server with reload enabled."""
    c.run("uvicorn src.peak_mentions.api.main:app --reload")
