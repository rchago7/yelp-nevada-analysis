-- Hive Queries Used in Project (CIS 4560 - Yelp Nevada Analysis)

-️- 1 Total number of Nevada businesses
SELECT COUNT(*) AS total_businesses
FROM yelp_business_nv;

️-- 2 Top 10 Nevada cities by business count
SELECT city, COUNT(*) AS total_businesses
FROM yelp_business_nv
GROUP BY city
ORDER BY total_businesses DESC
LIMIT 10;

-- ️3 Top categories in Nevada
SELECT categories, COUNT(*) AS total
FROM yelp_business_nv
GROUP BY categories
ORDER BY total DESC
LIMIT 10;

--️ 4 Highest rated cities (min 20 businesses)
SELECT city,
       ROUND(AVG(stars), 2) AS avg_rating,
       COUNT(*) AS num_businesses
FROM yelp_business_nv
GROUP BY city
HAVING COUNT(*) >= 20
ORDER BY avg_rating DESC
LIMIT 10;

-- ️5 Ratings distribution
SELECT stars, COUNT(*) AS total_businesses
FROM yelp_business_nv
GROUP BY stars
ORDER BY stars DESC;

-- 6️ Open vs closed businesses
SELECT is_open, COUNT(*) AS business_count
FROM yelp_business_nv
GROUP BY is_open;
