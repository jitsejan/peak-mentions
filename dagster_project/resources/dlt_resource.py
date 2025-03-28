from dagster import resource
from src.peak_mentions.connectors.dlt_pipeline import run_all

@resource
def dlt_resource(context):
    context.log.info("Running DLT pipeline")
    run_all()
    return "DLT pipeline run complete"