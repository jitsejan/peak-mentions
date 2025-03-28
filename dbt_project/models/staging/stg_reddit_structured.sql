WITH base AS (
  SELECT
    s._dlt_id,
    s.text,
    s.author,
    s.created_date,
    s.likes,
    NULL AS quote_tweet,
    NULL AS title,
    NULL AS heart_reaction,
    NULL AS angry_reaction,
    'reddit' AS platform,
    FALSE AS is_structured
  FROM {{ source('mentions_data', 'reddit_structured') }} s
),

media_joined AS (
  SELECT
    _dlt_parent_id,
    string_agg(value, ', ') AS media
  FROM {{ source('mentions_data', 'reddit_structured__media') }}
  GROUP BY _dlt_parent_id
)

SELECT
  b.text,
  b.author,
  b.created_date,
  m.media,
  b.likes,
  b.title,
  b.quote_tweet,
  b.heart_reaction,
  b.angry_reaction,
  b.platform,
  b.is_structured
FROM base b
LEFT JOIN media_joined m ON b._dlt_id = m._dlt_parent_id