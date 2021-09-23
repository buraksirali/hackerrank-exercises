-- Average Population --
SELECT ROUND(AVG(POPULATION), 0) FROM CITY;

-- Japan Population --
SELECT SUM(POPULATION) FROM CITY WHERE COUNTRYCODE = 'JPN';

-- Population Density Difference --
SELECT MAX(POPULATION) - MIN(POPULATION) FROM CITY;

-- The Sum Function --
SELECT SUM(POPULATION) FROM CITY WHERE DISTRICT = 'California';

-- The Average Function --
SELECT AVG(POPULATION) FROM CITY WHERE DISTRICT = 'California';

-- The Count Function --
SELECT COUNT(*) FROM CITY WHERE POPULATION > 100000;

-- The Blunder --
SELECT CAST(CEILING(AVG(CAST(Salary AS FLOAT)) - AVG(CAST(REPLACE(Salary, '0', '') AS FLOAT))) AS INT) FROM EMPLOYEES;

-- Earnings Of Employees --
DECLARE @max_earning AS INT = (SELECT MAX(salary * months) FROM Employee);
DECLARE @max_earner_count AS INT = (SELECT COUNT(employee_id) FROM Employee WHERE salary * months = @max_earning)

PRINT CAST(@max_earning AS VARCHAR) + ' ' + CAST(@max_earner_count AS VARCHAR);