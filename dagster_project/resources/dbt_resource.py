import os
from dagster_dbt import DbtCliResource

dbt_resource = DbtCliResource(
    project_dir=os.path.join(os.getcwd(), 'dbt_project'),
    profiles_dir=os.path.join(os.getcwd(), 'dbt_project'),
)