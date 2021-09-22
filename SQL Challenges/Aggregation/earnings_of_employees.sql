-- MS SQL Server Solution --
DECLARE @max_earning AS INT = (SELECT MAX(salary * months) FROM Employee);
DECLARE @max_earner_count AS INT = (SELECT COUNT(employee_id) FROM Employee WHERE salary * months = @max_earning)

PRINT CAST(@max_earning AS VARCHAR) + ' ' + CAST(@max_earner_count AS VARCHAR)