WITH ranked_movies AS (
  SELECT
    country,
    movie,
    ROW_NUMBER() OVER(PARTITION BY country ORDER BY COUNT(*) DESC) AS movie_rank
  FROM
    survey
  GROUP BY
    country, movie
)
SELECT
  country,
  STRING_AGG(movie, ', ')  as top3
FROM
  ranked_movies
WHERE
  movie_rank <= 3
GROUP BY  country


-- sample Result
--india	against_the_wind, harry-potter, dreamland
--france	breaking-bad, harry_potter, against_the_wind
--italy	against_the_wind, friends, dreamland