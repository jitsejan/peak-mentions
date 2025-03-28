import os
from dagster_dbt import dbt_assets, DbtCliResource

@dbt_assets(
    manifest=os.path.join(os.getcwd(), 'dbt_project', 'target', 'manifest.json'),
)
def run_all_dbt_models(context, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()