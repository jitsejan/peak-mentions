SELECT DISTINCT
    author,
    platform
FROM {{ ref('stg_mentions') }}
WHERE author IS NOT NULL