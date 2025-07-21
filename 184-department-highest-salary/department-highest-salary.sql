SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM employee e
JOIN department d ON e.departmentid = d.id
WHERE (e.departmentid, e.salary) IN (
    SELECT departmentid, MAX(salary)
    FROM employee
    GROUP BY departmentid
);
