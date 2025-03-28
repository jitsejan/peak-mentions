from dagster import Definitions
from dagster_project.jobs.dlt_job import dlt_extract_job
from dagster_project.assets.dbt_assets import run_all_dbt_models
from dagster_project.resources.dbt_resource import dbt_resource
from dagster_project.resources.dlt_resource import dlt_resource
from dagster import define_asset_job

dynamic_dbt_job = define_asset_job("dynamic_dbt_job", selection=[run_all_dbt_models])

defs = Definitions(
    jobs=[dlt_extract_job, dynamic_dbt_job],
    assets=[run_all_dbt_models],
    resources={
        "dbt": dbt_resource,
        "dlt_resource": dlt_resource
    },
)