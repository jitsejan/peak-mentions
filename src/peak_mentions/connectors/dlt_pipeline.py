import dlt
from peak_mentions.connectors.sources.facebook import facebook_source
from peak_mentions.connectors.sources.x import x_source
from peak_mentions.connectors.sources.reddit import reddit_source


def run_all():
    pipeline = dlt.pipeline(
        pipeline_name="mentions_pipeline",
        destination="duckdb",
        dataset_name="mentions_data"
    )

    load_info = pipeline.run([
        facebook_source(),
        x_source(),
        reddit_source()
    ])

    print(load_info)


if __name__ == "__main__":
    run_all()
