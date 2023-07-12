-- Task 1: Display first name, last name, department number, and department name for each employee
SELECT e.first_name, e.last_name, e.department_id, d.department_name
FROM employees e
JOIN department d ON e.department_id = d.department_id;

-- Task 2: Display first name, last name, department, city, and state province for each employee
SELECT e.first_name, e.last_name, d.department_name, l.city, l.state_province
FROM employees e
JOIN department d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id;

-- Task 3: Display first name, last name, department number, and department name for employees in departments 80 or 40
SELECT e.first_name, e.last_name, e.department_id, d.department_name
FROM employees e
JOIN department d ON e.department_id = d.department_id
WHERE e.department_id IN (80, 40);

-- Task 4: Display all departments, including those without any employees
SELECT d.department_id, d.department_name, e.first_name, e.last_name
FROM department d
LEFT JOIN employees e ON d.department_id = e.department_id;

-- Task 5: Display first name of employees and their managers
SELECT e.first_name AS employee_first_name, m.first_name AS manager_first_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id;

-- Task 6: Display job title, full name, and salary difference for each employee
SELECT j.job_title, e.first_name || ' ' || e.last_name AS full_name,
       (j.max_salary - e.salary) AS salary_difference
FROM employees e
JOIN jobs j ON e.job_id = j.job_id;

-- Task 7: Display job title and average salary of employees
SELECT j.job_title, AVG(e.salary) AS average_salary
FROM employees e
JOIN jobs j ON e.job_id = j.job_id
GROUP BY j.job_title;

-- Task 8: Display full name and salary of employees in London departments
SELECT e.first_name || ' ' || e.last_name AS full_name, e.salary
FROM employees e
JOIN department d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id
WHERE l.city = 'London';

-- Task 9: Display department name and number of employees in each department
SELECT d.department_name, COUNT(e.employee_id) AS employee_count
FROM department d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name;
