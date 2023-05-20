-- Query to display names (first_name, last_name) using alias name "First Name", "Last Name" from the employees table
SELECT first_name AS "First Name", last_name AS "Last Name" FROM employees;

-- Query to get the unique department ID from the employee table
SELECT DISTINCT department_id FROM employees;

-- Query to get all employee details from the employee table ordered by first name, descending
SELECT * FROM employees ORDER BY first_name DESC;

-- Query to get the names (first_name, last_name), salary, and PF (calculated as 12% of salary) of all employees
SELECT first_name, last_name, salary, salary * 0.12 AS PF FROM employees;

-- Query to get the maximum and minimum salary from the employees table
SELECT MAX(salary) AS max_salary, MIN(salary) AS min_salary FROM employees;

-- Query to get the monthly salary (rounded to 2 decimal places) of each employee
SELECT first_name, last_name, ROUND(salary / 12, 2) AS monthly_salary FROM employees;
