-- Average yearly gold price
SELECT
    EXTRACT(YEAR FROM date) AS year,
    AVG(price) AS avg_price
FROM gold_cleaned
GROUP BY year
ORDER BY year;

-- Yearly volatility
SELECT
    EXTRACT(YEAR FROM date) AS year,
    STDDEV(price) AS price_volatility
FROM gold_cleaned
GROUP BY year
ORDER BY year;
