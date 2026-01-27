# Database & SQL Concepts

## Basic Concepts

### What is a database, and why do we use it instead of spreadsheets or text files?

A database is an organized collection of data that can be easily stored, accessed, updated, and managed.

We use databases instead of spreadsheets or text files because:

- Databases handle large amounts of data efficiently
- Multiple users can access data at the same time
- Data is more secure and controlled
- Data consistency and accuracy are maintained
- Complex queries and relationships are supported

Spreadsheets are good for small, simple data. Databases are built for serious, long-term data storage.

---

### Difference between Data, Information, and Knowledge

- **Data**: Raw facts with no meaning  
  Example: `25, John, 5000`  

- **Information**: Processed data with meaning  
  Example: `John is 25 years old and earns 5000`  

- **Knowledge**: Understanding gained from information  
  Example: `People with this salary can afford product X`  

---

### Difference between DBMS and RDBMS

- **DBMS (Database Management System)**: Manages data in files or simple tables, no relationships between tables (example: file-based system)  
- **RDBMS (Relational DBMS)**: Stores data in related tables, uses primary keys and foreign keys, follows relational rules (example: MySQL, PostgreSQL, Oracle)  

---

### Common Types of Databases

- **Relational**: Tables with rows and columns (MySQL, PostgreSQL)  
- **NoSQL**: Flexible structure (MongoDB, Cassandra)  
- **Graph**: Focus on relationships (Neo4j)  
- **Time-series**: Time-based data (InfluxDB)  
- **Key-value**: Fast lookups (Redis)  

---

## Data Models & Structures

### What is a table in a relational database?

A table is a structured collection of data stored in rows and columns. Each table represents one entity, such as users, orders, or products.

---

### Definitions

- **Record (Row)**: One complete entry in a table  
- **Field (Column)**: One type of data (name, age, email)  
- **Schema**: The structure of the database (tables, columns, data types)  

---

### Primary Key

A primary key:

- Uniquely identifies each record  
- Cannot be NULL or duplicated  
- Ensures data integrity  

Example: `user_id`

---

### Foreign Key

A foreign key:

- Links one table to another  
- References the primary key of another table  
- Maintains relationships between tables  

Example: `order.user_id → users.user_id`

---

### Candidate Key vs Composite Key vs Surrogate Key

- **Candidate Key**: Any column that can uniquely identify a record  
  Example: `email` or `user_id` in `users` table  

- **Composite Key**: A key made of multiple columns  
  Example: `(student_id, course_id)` in an `enrollments` table  

- **Surrogate Key**: Artificial key created just to uniquely identify a record  
  Example: `id INT AUTO_INCREMENT`  

---

## Relationships

### Types of Relationships

- **One-to-One**: One record relates to one record  
- **One-to-Many**: One record relates to many records  
- **Many-to-Many**: Many records relate to many records  

---

### Real-life Examples

- One-to-One: Person → Passport  
- One-to-Many: Customer → Orders  
- Many-to-Many: Students ↔ Courses  

---

### How Joins Represent Relationships

Joins combine data from multiple tables based on related columns.  

Example:

```sql
SELECT users.name, orders.order_id
FROM users
INNER JOIN orders ON users.user_id = orders.user_id;


Normalization & Data Integrity
What is Normalization?

Normalization is the process of organizing data to:

Remove duplication

Improve consistency

Reduce update problems

Normal Forms

1NF (First Normal Form): No repeating groups, atomic values

2NF (Second Normal Form): No partial dependency on composite keys

Example: enrollments(student_id, course_id, student_name)

student_name depends only on student_id, not the full key (student_id, course_id)

Fix: Move student_name to a separate students table

3NF (Third Normal Form): No dependency on non-key columns

Example: employee(emp_id, emp_name, dept_id, dept_name)

dept_name depends on dept_id, not emp_id directly

Fix: Create a separate departments(dept_id, dept_name) table

What is Denormalization?

Denormalization:

Intentionally adds redundancy

Improves read performance

Used in reporting or analytics systems

Referential Integrity

Ensures that:

Foreign key values always match an existing primary key

Or are NULL if allowed

Example:

FOREIGN KEY (user_id) REFERENCES users(user_id)

Constraints

NOT NULL: Value must exist

UNIQUE: No duplicate values

CHECK: Validates conditions

DEFAULT: Sets a default value

SQL Concepts
DDL vs DML vs DCL

DDL (Data Definition Language): Defines structure (CREATE, ALTER, DROP)

DML (Data Manipulation Language): Manipulates data (INSERT, UPDATE, DELETE)

DCL (Data Control Language): Controls access (GRANT, REVOKE)

SELECT vs UPDATE

SELECT: Retrieves data

UPDATE: Modifies existing data

JOIN Types

INNER JOIN: Matching rows only

LEFT JOIN: All left table rows

FULL OUTER JOIN: All rows from both tables

WHERE vs HAVING

WHERE: Filters rows before grouping

SELECT * FROM students
WHERE age > 20;


HAVING: Filters groups after aggregation

SELECT department, COUNT(*) AS num_employees
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;

View vs Table

Table: Stores actual data

View: Virtual table based on a query

Views are used for:

Security

Simplified queries

Reusability