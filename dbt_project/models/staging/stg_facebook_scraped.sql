SELECT
    text,
    author,
    created_date,
    NULL AS media,
    likes,
    NULL AS title,
    NULL AS quote_tweet,
    heart_reaction,
    angry_reaction,
    'facebook' AS platform,
    FALSE AS is_structured
FROM {{ source('mentions_data', 'facebook_scraped') }}