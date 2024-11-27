
# Join, Group By, Window Functions

## Aggregate Functions
### COUNT, MAX, MIN, AVG, SUM
- **Usage**: Perform calculations on a set of values and return a single value.
- **When and Why Used**: Useful for summarizing data in queries (e.g., calculating totals, averages, or finding extremes).
  - COUNT: Counts rows.
  - MAX: Finds the maximum value.
  - MIN: Finds the minimum value.
  - AVG: Calculates the average.
  - SUM: Adds up values.
- **Common Mistakes**:
  - Using `COUNT(column_name)` incorrectly where null values are included unintentionally.
  - Misinterpreting results when used without `GROUP BY` (applies to the entire dataset).
  - Forgetting to alias the result for clarity.
- **Example**:
  ```sql
  SELECT COUNT(id), MAX(salary), AVG(age) FROM employees;
  ```

## GROUP BY
- **Usage**: Groups rows sharing a property and applies aggregate functions to each group.
- **When and Why Used**: To organize data into subsets for summarization (e.g., total sales by region).
- **How It Shouldn’t Be Used**:
  - Including columns in the SELECT clause not part of the GROUP BY or aggregate functions.
- **Common Mistakes**:
  - Using GROUP BY with SELECT * (returns ambiguous results).
  - Confusion between `WHERE` and `HAVING`.
- **Example**:
  ```sql
  SELECT department, AVG(salary) FROM employees GROUP BY department;
  ```

## HAVING
- **Usage**: Filters grouped data based on conditions.
- **When and Why Used**: To apply conditions on aggregated data (unlike WHERE).
- **Common Mistakes**:
  - Using HAVING instead of WHERE for row-level filters.
  - Combining HAVING with non-aggregated columns incorrectly.
- **Example**:
  ```sql
  SELECT department, AVG(salary)
  FROM employees
  GROUP BY department
  HAVING AVG(salary) > 50000;
  ```

## Order of Keywords in SQL Queries
1. SELECT
2. FROM
3. WHERE
4. GROUP BY
5. HAVING
6. ORDER BY
- **Common Mistakes**:
  - Misordering keywords (e.g., using HAVING before GROUP BY).

## Join and Natural Join

### INNER JOIN
- **Usage**: Combines rows from two tables when a match is found in both.
- **Example**:
  ```sql
  SELECT employees.name, departments.department_name
  FROM employees
  INNER JOIN departments ON employees.department_id = departments.id;
  ```

### NATURAL JOIN
- **Usage**: Automatically joins tables on columns with the same name.
- **When Used**: When column names and data types match.
- **Example**:
  ```sql
  SELECT * FROM employees NATURAL JOIN departments;
  ```
- **Common Mistakes**:
  - Using NATURAL JOIN with tables that have unintended column name matches.

### LEFT JOIN
- **Usage**: Retrieves all rows from the left table, with matching rows from the right table or NULLs.
- **Example**:
  ```sql
  SELECT employees.name, orders.order_date
  FROM employees
  LEFT JOIN orders ON employees.id = orders.employee_id;
  ```

### RIGHT JOIN
- **Usage**: Opposite of LEFT JOIN, retrieves all rows from the right table.
- **Example**:
  ```sql
  SELECT employees.name, orders.order_date
  FROM employees
  RIGHT JOIN orders ON employees.id = orders.employee_id;
  ```

### FULL OUTER JOIN
- **Usage**: Combines LEFT JOIN and RIGHT JOIN, including unmatched rows from both tables.
- **Example**:
  ```sql
  SELECT employees.name, orders.order_date
  FROM employees
  FULL OUTER JOIN orders ON employees.id = orders.employee_id;
  ```

## Sub-Queries (Nested or Inner Queries)
- **Usage**: A query inside another query.
- **Types**: Scalar, single-row, multi-row, correlated sub-queries.
- **When Used**: For dynamic filtering or deriving intermediate data.
- **Examples**:
  - **IN**:
    ```sql
    SELECT name FROM employees WHERE department_id IN (SELECT id FROM departments WHERE location = 'NY');
    ```
  - **EXISTS**:
    ```sql
    SELECT name FROM employees WHERE EXISTS (SELECT 1 FROM departments WHERE employees.department_id = departments.id);
    ```

## CRUD Operations

### CREATE
- **Usage**: Creates a new table or database.
- **Example**:
  ```sql
  CREATE TABLE employees (id INT PRIMARY KEY, name VARCHAR(50), salary DECIMAL);
  ```

### READ (SELECT)
- **Usage**: Retrieves data from a database.
- **Example**:
  ```sql
  SELECT * FROM employees WHERE salary > 50000;
  ```

### UPDATE
- **Usage**: Modifies existing data.
- **Example**:
  ```sql
  UPDATE employees SET salary = salary * 1.1 WHERE department_id = 1;
  ```

### DELETE
- **Usage**: Removes rows from a table.
- **Example**:
  ```sql
  DELETE FROM employees WHERE salary < 20000;
  ```

## DROP and TRUNCATE

### DROP
- **Usage**: Permanently removes a table or database.
- **Example**:
  ```sql
  DROP TABLE employees;
  ```
- **Caution**: Cannot be rolled back.

### TRUNCATE
- **Usage**: Deletes all rows in a table but retains the table structure.
- **Example**:
  ```sql
  TRUNCATE TABLE employees;
  ```
- **Differences from DELETE**:
  - Faster as it does not log individual row deletions.
  - Cannot include a WHERE clause.

## Best Practices
1. Use meaningful aliases for columns and tables.
2. Avoid SELECT * in production queries for better performance.
3. Test JOINs and sub-queries on smaller datasets to verify correctness.
4. Ensure indexes are used for JOINs and WHERE conditions to optimize performance.
5. Always back up data before using DROP or TRUNCATE.
