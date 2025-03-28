SELECT
    author,
    platform,
    CASE
        WHEN created_date = 'Yesterday' THEN CURRENT_DATE - INTERVAL '1 day'
        WHEN created_date = 'Today' THEN CURRENT_DATE
        WHEN created_date NOT LIKE '____-__-__' THEN NULL
        ELSE CAST(created_date AS DATE)
    END AS created_date,
    COUNT(*) AS post_count,
    SUM(
        CASE 
            WHEN likes ~ '^\d+$' THEN CAST(likes AS BIGINT)
            ELSE 0 
        END
    ) AS total_likes,
    AVG(
        CASE 
            WHEN likes ~ '^\d+$' THEN CAST(likes AS BIGINT)
            ELSE 0
        END
    ) AS avg_likes
FROM {{ ref('stg_mentions') }}
WHERE likes IS NOT NULL
GROUP BY author, platform, created_date