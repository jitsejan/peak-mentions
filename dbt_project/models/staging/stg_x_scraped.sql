SELECT
    text,
    author,
    created_date,
    NULL AS media,
    likes,
    NULL AS title,
    quote_tweet,
    NULL AS heart_reaction,
    NULL AS angry_reaction,
    'x' AS platform,
    FALSE AS is_structured
FROM {{ source('mentions_data', 'x_scraped') }}