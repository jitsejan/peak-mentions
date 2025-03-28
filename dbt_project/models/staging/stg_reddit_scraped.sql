SELECT
    text,
    author,
    created_date,
    NULL AS media,
    NULL AS likes,
    title,
    NULL AS quote_tweet,
    NULL AS heart_reaction,
    NULL AS angry_reaction,
    'reddit' AS platform,
    FALSE AS is_structured
FROM {{ source('mentions_data', 'reddit_scraped') }}