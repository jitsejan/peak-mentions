SELECT
    REGEXP_EXTRACT(text, '(https?://[^\s]+)') AS url,
    platform,
    COUNT(*) AS mention_count
FROM {{ ref('stg_mentions') }}
WHERE text ILIKE '%http%'
GROUP BY url, platform
ORDER BY mention_count DESC