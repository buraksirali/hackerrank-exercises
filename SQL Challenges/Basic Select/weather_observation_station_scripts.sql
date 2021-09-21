-- MS SQL Server Solution --

-- Script 1 --
SELECT CITY, STATE FROM STATION;

-- Script 3 --
SELECT DISTINCT CITY FROM STATION WHERE ID % 2 = 0;

-- Script 4 --
SELECT COUNT(CITY) - COUNT(DISTINCT CITY) FROM STATION;

-- Script 5 --
SELECT TOP 1 CITY, LEN(CITY) FROM STATION ORDER BY LEN(CITY) ASC, CITY ASC;
SELECT TOP 1 CITY, LEN(CITY) FROM STATION ORDER BY LEN(CITY) DESC, CITY ASC;

-- Script 6 --
SELECT DISTINCT CITY FROM STATION WHERE LEFT(CITY, 1) IN ('a', 'e', 'i', 'o', 'u');

-- Script 7 --
SELECT DISTINCT CITY FROM STATION WHERE RIGHT(CITY, 1) IN ('a', 'e', 'i', 'o', 'u');

-- Script 8 --
SELECT DISTINCT CITY FROM STATION 
WHERE 
LEFT(CITY, 1) IN ('a', 'e', 'i', 'o', 'u')
AND 
RIGHT(CITY, 1) IN ('a', 'e', 'i', 'o', 'u');

-- Script 9 --
SELECT DISTINCT CITY FROM STATION WHERE LEFT(CITY, 1) NOT IN ('a', 'e', 'i', 'o', 'u');

-- Script 10 --
SELECT DISTINCT CITY FROM STATION WHERE RIGHT(CITY, 1) NOT IN ('a', 'e', 'i', 'o', 'u');

-- Script 11 --
SELECT DISTINCT CITY FROM STATION 
WHERE 
LEFT(CITY, 1) NOT IN ('a', 'e', 'i', 'o', 'u')
OR
RIGHT(CITY, 1) NOT IN ('a', 'e', 'i', 'o', 'u');

-- Script 12 --
SELECT DISTINCT CITY FROM STATION 
WHERE 
LEFT(CITY, 1) NOT IN ('a', 'e', 'i', 'o', 'u')
AND
RIGHT(CITY, 1) NOT IN ('a', 'e', 'i', 'o', 'u');