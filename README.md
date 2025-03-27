# peak-mentions
A robust, local data pipeline using modern Python data engineering tools.

## Virtual environment
To run this project the package manager [Rye](https://rye.astral.sh) is used. To activate the virtual environment on Mac for fish shell, run the following:

```sh
$ cd peak-mentions
$ rye sync
$ . ./.venv/bin/activate.fish 
```

## Project setup
- Data generation ([fastapi](https://fastapi.tiangolo.com) + [polyfactory](https://polyfactory.litestar.dev/latest/)). 
- Data ingestion  ([dlt](https://dlthub.com))
- Orchestration ([dagster](https://dagster.io))
- Data transformation ([dbt](https://www.getdbt.com))
- Testing ([pytest](https://docs.pytest.org/en/stable/))

For storage [DuckDB](https://duckdb.org) is used as local database.
