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

## Data generation
For the data generation six endpoints are created with FastAPI. The three sources are for:

- Facebook
- Reddit
- X

and for each source there are two endpoints:

- api
- scraped

The data from the api is structured where the scraped endpoints return semi-structured data. The endpoints are defined under `api/endpoints`.

Based on the schema description different models are created under `api/models` for the three different sources and two factories for each to create both the structured and unstructured data under the `api/factories` folder.

Finally, the server to expose the API is defined in `api/main.py` and includes routers to the endpoint. All the endpoints will trigger the data factory and create dummy data to be consumed.

### Running the server
To run the server the following command is used:

```bash
$ uvicorn src.peak_mentions.api.main:app --reload
```

Or alternatively, use the `fabfile.py` with the command:

```bash
$ fab run-fastapi
```

### Querying the data

The data can now be queried locally on `localhost:8000/`. Explore the API by navigating to `http://localhost:8000/docs` and try the endpoints:

![Docs for API](img/peakmention_swagger.png)

Or use an API client to explore the data:

![Endpoints for pipeline](img/peakmention_httpie.png)

## Data ingestion

To load data from the endpoints created in the previous step the ingestion package `dlt` is used. For each source (Facebook, Reddit, X) a connector is build where the different endpoints (resources) are defined. The data is loaded into a DuckDB Database.

### Running the ingestion
In order to execute the ingestion job, run the following command:

```bash
$ python src/peak_mentions/connectors/dlt_pipeline.py
```

Or alternatively, use Fabric again:

```bash
$ fab ingest-all
```

### Validating the data

After running the ingestion, the data can be validated using the DuckDB UI (or loaded into most popular database viewers).

Running

```bash
$ duckdb --ui mentions_pipeline.duckdb
```

will open a browser with the DuckDB interface that contains a table viewer and a notebook environment.

![DuckDB interface](img/duckdb_ui.png)

Alternatively, run the following to get the UI:

```bash
$ fab duckdb-ui
```
