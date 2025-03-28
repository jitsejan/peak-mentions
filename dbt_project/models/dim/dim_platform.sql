SELECT DISTINCT
    platform
FROM {{ ref('stg_mentions') }}