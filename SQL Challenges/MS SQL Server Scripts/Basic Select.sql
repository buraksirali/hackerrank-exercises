-- Select All --
SELECT * FROM CITY;

-- Select By Id --
SELECT * FROM CITY WHERE ID = 1661;

-- Revising the Select Query --
SELECT * FROM CITY WHERE POPULATION > 100000 AND COUNTRYCODE = "USA";

-- Revising the Select Query 2 --
SELECT NAME FROM CITY WHERE COUNTRYCODE = "USA" AND POPULATION > 120000;

-- Name Of Employees --
SELECT NAME FROM EMPLOYEE ORDER BY NAME;

-- Salary of Employees --
SELECT NAME FROM EMPLOYEE WHERE SALARY > 2000 AND MONTHS < 10 ORDER BY EMPLOYEE_ID ASC;

-- Japanese Cities Attributes --
SELECT * FROM CITY WHERE COUNTRYCODE = "JPN";

-- Japanese Cities Name --
SELECT NAME FROM CITY WHERE COUNTRYCODE='JPN';

-- More Than 75 Marks --
SELECT Name FROM STUDENTS WHERE MARKS > 75 ORDER BY RIGHT(Name, 3), ID ASC;