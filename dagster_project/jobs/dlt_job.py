from dagster import op, job, Output

@op(required_resource_keys={"dlt_resource"})
def extract_data_with_dlt(context):
    result = context.resources.dlt_resource
    context.log.info(f"DLT returned: {result}")
    return Output(result)

@job
def dlt_extract_job():
    extract_data_with_dlt()