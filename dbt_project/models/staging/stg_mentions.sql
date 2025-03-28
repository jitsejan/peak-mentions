SELECT * FROM {{ ref('stg_facebook_structured') }}
UNION ALL
SELECT * FROM {{ ref('stg_facebook_scraped') }}
UNION ALL
SELECT * FROM {{ ref('stg_x_structured') }}
UNION ALL
SELECT * FROM {{ ref('stg_x_scraped') }}
UNION ALL
SELECT * FROM {{ ref('stg_reddit_structured') }}
UNION ALL
SELECT * FROM {{ ref('stg_reddit_scraped') }}