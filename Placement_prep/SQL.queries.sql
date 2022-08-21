
-- Data is nothing but facts and statistics stored or free flowing over a network

-- The database is a collection of inter-related data which is used to retrieve, insert and delete the data efficiently
-- Using the database, you can easily retrieve, insert, and delete the information
-- Advantages of DBMS
-- 1. Controls database redundancy
-- 2. Data sharing
-- 3. Data security
-- 4. Easily Maintenance
-- 5. Backup

-- Disadvantages of DBMS
-- 1. Cost of Hardware and Software
-- 2. Complexity: Database system creates additional complexity and requirements.
-- 3. Higher impact of failure


--  column and table names are not case sensitive    , Usre and user treats as same 
--  string should be in single quotes only '' , not " " accepted in queries , avoid using "" in queries
--  Rahul and rahul are not same in case of values , but same in case of column names as they are not case insensitive

-- ease the user interaction with database, the developers hide internal irrelevant details from users. 
-- This process of hiding irrelevant details from user is called data abstraction.

-- We have three levels of abstraction:
-- Physical level: This is the lowest level of data abstraction. It describes how data is actually stored in database. 
--                      You can get the complex data structure details at this level.
-- Logical level: This is the middle level of 3-level data abstraction architecture. It describes what data is stored in database.
-- View level: Highest level of data abstraction. This level describes the user interaction with database system.


-- ACID Properties are used for maintaining the integrity of database during transaction processing.
--  ACID in DBMS stands for Atomicity, Consistency, Isolation, and Durability.

-- • Atomicity: A transaction is a single unit of operation. You either execute it entirely or do not execute it at all. There cannot be partial execution.
-- • Consistency: Once the transaction is executed, it should move from one consistent state to another.
-- • Isolation: Transaction should be executed in isolation from other transactions (no Locks). During concurrent transaction execution, intermediate transaction results from simultaneously executed transactions should not be made available to each other. (Level 0,1,2,3)
-- • Durability: · After successful completion of a transaction, the changes in the database should persist. Even in the case of system failures.


-- TYPES OF DBMS ARCHITECTURE

--  1. Single Server Architecture -> database is in application server , mainly used in development phase
--  2. Two Tiew Architecture -> database and application is in two separate servers , application connection interface such as JDBC, ODBC are used
                                -- application is responsible for data access and data manipulation
-- 3. Three Tier Architecture -> client application doesn’t communicate directly with the database systems present at the server machine, 
--                                rather the client application communicates with server application and the server application internally communicates with the database system present at the server


-- Database languages are used to read, update and store data in a database. 
-- There are several such languages that can be used for this purpose; one of them is SQL (Structured Query Language).

-- SQL / DATABASE Statements :

-- • DDL - Data Definition Language:       (CREATE,DROP,ALTER,TRUNCATE,COMMENT,RENAME)
-- • DML - Data Manipulation Language:         (INSERT, UPDATE,DELETE)
-- • DCL - Data Control Language:            (GRANT,REVOKE)  GRANT-gives user’s access privileges to database. REVOKE-withdraw user’s access privileges given by using the GRANT command
-- • TCL - Transaction Control Language:            (COMMIT,ROLLBACK ,SAVEPOINT) SAVEPOINT–sets a savepoint within a transaction


-- DROP : DROP is used to delete a whole database or just a table.
--              The DROP statement destroys the objects like an existing database, table, index, or view.
--              Table or Database deletion using DROP statement cannot be rolled back, so it must be used wisely

-- TRUNCATE : It is used to remove all records from a table, including all spaces but it does not alter table structure .
--              The TRUNCATE TABLE mytable statement is logically (though not physically) equivalent to the DELETE FROM mytable statement (without a WHERE clause).

--  Keys help you to identify any row of data in a table. Keys ensure that you can uniquely identify a table record despite any challenges
-- seven different types of Keys in DBMS and each key has its different functionality:
-- • Super Key - A super key is a group of single or multiple keys which identifies rows in a table.
-- • Primary Key - is a column or group of columns in a table that uniquely identify every row in that table.
-- • Candidate Key - is a set of attributes that uniquely identify tuples in a table. Candidate Key is a super key with no repeated attributes.
-- • Alternate Key - is a column or group of columns in a table that uniquely identify every row in that table.
-- • Foreign Key - is a column that creates a relationship between two tables. The purpose of Foreign keys is to maintain data integrity and allow navigation between two different instances of an entity.
-- • Compound Key - has two or more attributes that allow you to uniquely recognize a specific record. It is possible that each column may not be unique by itself within the database.
-- • Composite Key - An artificial key which aims to uniquely identify each record is called a surrogate key. These kind of key are unique because they are created when you don't have any natural primary key.
-- • Surrogate Key - An artificial key which aims to uniquely identify each record is called a surrogate key. These kind of key are unique because they are created when you don't have any natural primary key.


-- ER model
-- ER model stands for an Entity-Relationship model. 
-- It is a high-level data model. This model is used to define the data elements and relationship for a specified system.  
-- It develops a conceptual design for the database. It also develops a very simple and easy to design view of data.


--                                  SELECT  -> DML 
--                                      word Manipulation means , such statement allows both data accessing and processing so SELECT is DML

SELECT * FROM users;    -- get all users

SELECT names,addr FROM users;    -- get names and addr of all users

SELECT DISTINCT names FROM users;    -- get all distinct/unique names , no duplicates

SELECT * FROM users WHERE id = 1;    -- get user with id 1

SELECT * FROM users WHERE (id % 2) = 0;    -- get all users with id is even

SELECT * FROM users WHERE names = 'rahul';        -- get user with name rahul    

SELECT * FROM users WHERE names <> 'rahul';        --  get all users with name not equal to rahul            
 
SELECT * FROM users WHERE names = 'Rahul' AND id = 1;    -- get user with name Rahul and id 1         

SELECT * FROM users WHERE names = 'rahul' AND id = 1 AND age = 20;    -- get user with name rahul and id 1 and age 20

SELECT * FROM users WHERE names = 'rahul' AND (id = 1 OR age = 20);    -- get user with name rahul and id 1 or age 20

SELECT * FROM users WHERE names = 'rahul' OR id = 1;        -- get user with name rahul or id 1 

SELECT * FROM users WHERE NOT names = 'rahul' ;        -- get all users except rahul

SELECT CONCAT(names," addr is :",addr , "end") FROM users;    -- get names and addr of all users concatenated as e.g.  rahul addr is : abc end for every record

--                    IN       - shorthand for multiple OR conditions , used in WHERE clause or another select clause

SELECT * FROM users WHERE names IN ('rahul','suresh');        -- get users with names rahul or suresh

SELECT * FROM users WHERE names NOT IN ('rahul','suresh');        -- get users with names not rahul or suresh

SELECT * FROM users WHERE names IN (SELECT names FROM lucky_users);     -- get users with names from lucky_users


--                   BETWEEN  - used in WHERE clause with AND operator

SELECT * FROM users WHERE age BETWEEN 20 AND 30;        -- get users with age between 20 and 30 , age can be 10 and also 20 ,both are included

SELECT * FROM users WHERE age NOT BETWEEN 20 AND 30;        -- get users with age not between 20 and 30

SELECT * FROM users WHERE birthdates BETWEEN '1990-01-01' AND '2000-01-01';        -- get users with birthdates between 1990-01-01 and 2000-01-01

--                   AS      - used in SELECT clause to rename column name , also known as alias , can be used with column name , table name , function name , arithmetic expression

SELECT names AS user_name,addr AS user_addr FROM users;        -- get names as user_name and addr as user_addr

--                    Order by - sort the result-set in ascending or descending order , by default it is ascending

SELECT * FROM users ORDER BY names;    -- get all users in alphabetical order , same as SELECT * FROM users ORDER BY names ASC 

SELECT * FROM users ORDER BY LENGTH(names) DESC;    -- get all users in descending order of length of names , longest name first

SELECT * FROM users ORDER BY names DESC;    -- get all users in reverse alphabetical order

SELECT * FROM Customers ORDER BY Country ASC, CustomerName DESC; -- get all customers in alphabetical order by country and then by customer name in reverse order

--                    Group by - groups rows that have the same values into summary rows, like "find the number of customers in each country".
                                -- often used with aggregate functions

SELECT addr, COUNT(names) FROM users GROUP BY addr;    -- get addr and count of names in each addr like 3 people have addr of pune


--                      HAVING    -  WHERE keyword cannot be used with aggregate functions so HAVING is used 

SELECT addr, COUNT(names) FROM users GROUP BY addr HAVING COUNT(names) > 1;    -- get addr and count of names but only if count of names for same addr is greater than 1


--                      NULL          -  test for NULL values with comparison operators, such as =, <, or <>

SELECT * FROM users WHERE names IS NULL;    -- get all users where names is NULL

SELECT * FROM users WHERE names IS NOT NULL;    -- get all users where names is not NULL means there is a value

SELECT IFNULL(names,"notAname") FROM users ;    -- get names if it is not NULL else get "notAname"

--                      LIMIT        -  MySQL supports the LIMIT clause to select a limited number of records , other databases have another way to do this

SELECT * FROM users LIMIT 10;    -- get first 10 users

SELECT * FROM Customers WHERE Country='Germany' LIMIT 3; -- get first 3 customers from Germany

--                      LIKE          - LIKE operator is used in a WHERE clause to search for a specified pattern in a column

SELECT * FROM users WHERE names LIKE '%hul%';    -- get all users with names containing hul

                                    --  patterns :    
                                               --   "%" - match any number of characters
                                               --   "_" - match a single character
                                               --   "a%" - match a string starting with a
                                               --   "%a" - match a string ending with a
                                               --   "%a%" - match a string containing a
                                               --   "a_" - match a string starting with a and ending with anything like aa , ay
                                               --   "a%a" - match a string starting with a and ending with a
                                               --    "a__%" - match a string starting with a and have minimum 2 characters after a 

-- regular expressions can be used in like a LIKE clause , can be used with not operator e.g.  WHERE names NOT REGEXP '^abc';

SELEct * FROM users WHERE names REGEXP '^abc';    -- get all users with names starting with a or b or c

                                               --    '^ab'    - match a string starting with ab  like ab , abba , abti
                                               --     'ye?'    - match a string starting with ye and then have 0 or 1 character after like ye , yes
                                               --    'ed$'     - match a string ending with ed like liked
                                               --     'sh'     - match a string starting with sh like sh , sheep , sheepdog , kashmir
                                               --     '[a-d].'   - match a string starting with a or b or c or d and have any single character after it
                                               --    '^[a-d]'   - match a string starting with a or b or c or d
                                               --    '[sv]$'    - match a string ending with s or v like s , v , likes


--                      EXISTS      -  used in WHERE clause to test for the existence of any record in a subquery , returns TRUE if the subquery returns one or more records

SELECT * FROM users WHERE EXISTS (SELECT * FROM lucky_users);    -- get all users whos name is in lucky_users

--                     IF 

SELECT * FROM users WHERE names = IF(names = 'rahul', 'rahul is here', 'rahul is not here');    -- get all users with names rahul if it is rahul else get rahul is not here

SELECT IF(win_money > 1000 , "winner", "loser") FROM users;    -- get all users with win_money greater than 1000 as winner else loser

--                     UPPER and LOWER

SELECT UPPER(names) FROM users;    -- get all users with names in upper case

SELECT LOWER(names) FROM users;    -- get all users with names in lower case


--                     ANY , ALL        - allows perform a comparison between a single column value and a range of other values

        -- ANY - returns true if any of subquery values matches the  value in range

SELECT * FROM users WHERE names = ANY (SELECT names FROM lucky_users WHERE price > 1000);    -- get all users whose name is in lucky_users who has price greater than 1000


        -- ALL - returns true if all of subquery values matches the  value in range

SELECT * FROM users WHERE names = ALL (SELECT names FROM lucky_users WHERE price > 1000);    -- get all users whose name is in lucky_users who has price greater than 1000
                                                                                            -- only if all the records in subquery have price equal then only return true
                                                                            -- if all records in subquery have same names then return true

    -- diff between ANY and ALL is that ANY returns true if any of the records in subquery matches the value in range ,
        --  while ALL returns true if all of the records in subquery matches the value in range


--                     SELECT INTO       - copies data from one table into a new table.

SELECT * INTO CustomersBackup2017 FROM Customers;   -- copy data from Customers to CustomersBackup2017 in same database

SELECT * INTO CustomersBackup2017 IN 'Backup.mdb' FROM Customers;  -- copy data from Customers to CustomersBackup2017 in different database

--                     SELECT with CASE  - used to create a new column based on another column value

SELECT names, 
        CASE 
                WHEN price > 1000 THEN 'expensive'           -- when and then -> when condition then result
                WHEN price > 500 THEN 'medium'
                ELSE 'cheap'                                 --  default result
        END AS price_type                                    -- new column name where result is stored based on condition
        
        FROM users;    -- return names and price_type column with condition


--                                 CREATE

CREATE DATABASE databasename;    -- create a database , DROP DATABASE dbname to delete a database

CREATE TABLE users (names VARCHAR(20), addr VARCHAR(20), price INT);    -- create a table , DROP TABLE tablename to delete a entire table




--                                 ALTER       - modify existing table

ALTER TABLE users ADD COLUMN price INT
                  DROP COLUMN price
                  MODIFY COLUMN names  VARCHAR(10);    -- add , drop , modify a column in a table


--                                 INSERT

INSERT INTO users (names,addr) VALUES ('rahul','pune');    -- insert new user with name rahul and addr pune
 
--                                 INSERT INTO SELECT   - copies data from one table and inserts it into another table.

INSERT INTO users (names,addr) SELECT names,addr FROM lucky_users;    -- insert all users from lucky_users into users



--                                 UPDATE       - compulsory to use WHERE clause to update a record , If you omit the WHERE clause, ALL records will be updated

UPDATE users SET addr = 'pune' WHERE names = 'rahul';    -- update addr of user with name rahul to pune

--                                 DELETE       - Notice the WHERE clause ,  If you omit the WHERE clause, all records in the table will be deleted!

DELETE FROM users WHERE names = 'rahul';    -- delete user with name rahul

DELETE FROM users ;    -- delete all users ,  used for delete all rows in a table without deleting the table

TRUNCATE TABLE users;    -- delete all rows in a table , not delete the table




--                                  JOIN       - used to join two or more tables
-- The goal of creating a join condition is that it helps you to combine the data from two or more DBMS tables.
 
--    Inner Join       - returns all records from both tables that have matching values in both tables  , it is default join type

        (SELECT * FROM users WHERE names = 'rahul')   -- select all users with name rahul
INNER JOIN (SELECT * FROM lucky_users WHERE price > 1000)   -- select all users from lucky_users with price greater than 1000 , if requires all recordds then just type table name instead of (SELECT * FROM lucky_users)
                ON users.names = lucky_users.names;   -- on condition that users.names = lucky_users.names

        --  query can return Ambiguous column name error ,if same column is in both tables and we didnt used *  , then we can use alias to differentiate them

        e.g. SELECT users.names, lucky_users.price FROM users INNER JOIN lucky_users ON users.names = lucky_users.names;



--  Left Join       - returns all records from the left table with matching values in the right table , if there is no matching record in the right table , then it returns NULL for right table column

        (SELECT * FROM users WHERE names = 'rahul')   -- select all users with name rahul
        LEFT JOIN (SELECT * FROM lucky_users WHERE price > 1000)   -- select all users from lucky_users with price greater than 1000
                ON users.names = lucky_users.names;   -- on condition that users.names = lucky_users.names


--  Right Join       - returns all records from the right table that have matching values in the left table

        (SELECT * FROM users WHERE names = 'rahul')   -- select all users with name rahul
        RIGHT JOIN (SELECT * FROM lucky_users WHERE price > 1000)   -- select all users from lucky_users with price greater than 1000
                ON users.names = lucky_users.names;   -- on condition that users.names = lucky_users.names

--  Outer Join       - returns all records from both tables that have matching values in both tables
--                  also known as Full Join , FULL JOIN is the result of a combination of both left and right outer join
--                  It puts NULL on the place of matches not found

        (SELECT * FROM users WHERE names = 'rahul')   -- select all users with name rahul
        OUTER JOIN (SELECT * FROM lucky_users WHERE price > 1000)   -- select all users from lucky_users with price greater than 1000
                ON users.names = lucky_users.names;   -- on condition that users.names = lucky_users.names

-- window function in MySQL used to do a calculation across a set of rows that are related to the current row. also known as analytic function
-- window functions do not produce a result to be grouped into one row


--              Union      - returns all records from both tables

        (SELECT * FROM users WHERE names = 'rahul')   -- select all users with name rahul
        UNION (SELECT * FROM lucky_users WHERE price > 1000);   -- select all users from lucky_users with price greater than 1000

--         Union All       - returns all records from both tables , but it does not remove duplicate records

        (SELECT * FROM users WHERE names = 'rahul')   -- select all users with name rahul
        UNION ALL (SELECT * FROM lucky_users WHERE price > 1000);   -- select all users from lucky_users with price greater than 1000

        -- things to remember before using UNION and UNION ALL

                    -- UNION and UNION ALL can be used only on SELECT queries that have the same number of columns in both queries
                    -- both corresponding columns must have the same data type i.e. col1 in Q1 and col1 in Q2 must be of same data type
                    -- use * in both queries only if above conditions are met
                    -- union does not shows duplicate records i.e. every record in Q1 will be returned only once , even if it is present in Q2

--           Intersect      - returns all records that are present in both tables i.e returns the common rows from both the SELECT statements.

        (SELECT * FROM users WHERE names = 'rahul')   -- select all users with name rahul
        INTERSECT (SELECT * FROM lucky_users WHERE price > 1000);   -- select all users from lucky_users with price greater than 1000


--           Minus        - returns all records that are present in the first table and not present in the second table
                        --  Minus operator is used to display the rows which are present in the first query but absent in the second query. 
                        -- o It has no duplicates and data arranged in ascending order by default.

        (SELECT * FROM users WHERE names = 'rahul')   -- select all users with name rahul
        MINUS (SELECT * FROM lucky_users WHERE price > 1000);   -- select all users from lucky_users with price greater than 1000
        --  it will display all the records from users table which are not present in lucky_users table

--  Nested Query       - used to execute a query inside another query , The result of inner query is used in execution of outer query.

SELECT * FROM (SELECT * FROM users WHERE names = 'rahul') AS T1;   -- select all users with name rahul

--  Views      - are used to create a temporary table that can be used to store data temporarily.
--                   Views in SQL are considered as a virtual table. A view also contains rows and columns of the underlying table.
--     Uses of a View
--                    1. Restricting data access
--                    2. Hiding data complexity
--                    3. Simplify commands for the user
--                    4. Rename Columns -> rename the columns without affecting the base tables
--                   Views are created using CREATE VIEW statement.
--           Syntax      - CREATE VIEW view_name AS select_statement;

CREATE VIEW users_view AS SELECT * FROM users;    -- create a view called users_view that contains all users

--  view with multiple table
CREATE VIEW users_view AS SELECT users.names, lucky_users.price FROM users INNER JOIN lucky_users ON users.names = lucky_users.names;    -- create a view called users_view that contains all users with name and price from lucky_users


-- 3 Types of Window Function

        -- Aggregate Functions
        -- It is a function that operates on multiple rows and produces the result in a single row. Some of the important aggregate functions are:
                 -- COUNT, SUM, AVG, MIN, MAX, and many more.

        -- Ranking Functions
        -- It is a function that allows us to rank each row of a partition in a given table. Some of the important ranking functions are:
                -- RANK, DENSE_RANK, PERCENT_RANK, ROW_NUMBER, CUME_DIST, etc.

        -- Analytical Functions
        -- It is a function, which is locally represented by a power series. Some of the important analytical functions are:
                -- NTILE, LEAD, LAG, NTH, FIRST_VALUE, LAST_VALUE, etc.



--                                  Aggregate Functions -  only works with select queries
--         SQL aggregation function is used to perform the calculations on multiple rows of a single column of a table. It returns a single value

SELECT SUM(age) FROM users;    -- get total sum of all ages

SELECT MIN(Price) FROM Products;  

SELECT MIN(Price) FROM Products;  

SELECT MIN(Price) AS SmallestPrice FROM Products;    -- print smallest price with name SmallestPrice

SELECT COUNT(ProductID) FROM Products;   -- COUNT() function returns the number of rows that matches a specified criterion. can be used with where clause
                                        -- COUNT(*) that returns the count of all the rows in a specified table
SELECT COUNT(DISTINCT Country) FROM Customers;    --  can be used with distinct

SELECT COUNT(names) - COUNT(DISTINCT names) FROM users;    --  get number of users without unique names

SELECT AVG(Price) FROM Products;     -- AVG() function returns the average value of a specified column. can be used with where clause

SELECT LENGTH(names) FROM users;    -- LEN() function returns the length of a string. LENGTH used in MySQL is equivalent to CHAR_LENGTH in Oracle

SELECT LENGTH('rahul');        --  can be used with string , returns 5

SELECT names FROM users WHERE SUBSTRING(names,1,3) = 'rah';    -- SUBSTRING() function returns a part of a string. substring(string,start,length)
                                                                --  MYSQLTEAM    => SUBSTRING(names,1,3)  is MYS
                                                                --  MYSQLTEAM    => SUBSTRING(names,2,1)  is Y

SELECT names FROM users  ORDER BY SUBSTRING(names,2,1) ;     -- ORDER BY second character in names alphabetically

SELECT ROUND(Price,2) FROM Products;    -- ROUND() function returns a number rounded to a specified number of decimal places. e.g. 12.36 not 12.36894


--                       OVER - if used , sql engine treats aggregate functions as window functions meaning that they are calculated across a set of rows that are related to the current row.
                                -- always used with window functions like      window function(aggregate function) OVER (CLAUSE)
                                -- if nothing mentioned in OVER() , it will consider every single row in the partition as a single window
                                -- mutiple over clause in single query results in multiple windows but one window per one over clause 

SELECT * , max(price) over() as max_price FROM users ;    -- it will as  new col named max_price and conatins max price of all users
                                                        -- to get max price based on a column , use OVER(PARTITION BY column)



--                        PARTITION BY    - partition rows of table into groups , useful when we have to perform a calculation on individual rows of a group using other rows of that group.
                                         -- It is always used inside OVER() clause

SELECT * , count(*) OVER (PARTITION BY age) FROM users;    -- get all users with age and count of rows with same age in a same group as age
                                                        -- if count(*) directly used then it will return only 1 record with new column of count
 -- diff betn group by and partition by is that group by will group rows based on the value of mentioned column with single record , 
                                             -- while partition by will group rows based on the value of mentioned column for all available records

SELECT names , addr , max(price) OVER (PARTITION BY age) AS max_win_price FROM users;    -- new column named as max_win_price containing max price of each group of rows with same age

SELECT names , addr , max(price) OVER (PARTITION BY age order by names) AS max_win_price FROM users;  --- after partition , order by names , then max price will be returned

--                                  Ranking Functions - return a ranking value for each row in a partition.

-- ROW_NUMBER() function returns the row number of the current row in the partition.
-- if nothing is in over following row_number() , it will consider every single row in the partition as a single window and numbered as 1,2,3,4,5,6,7,8,9,10,-- sequentially

SELECT names , addr , max(price) OVER (PARTITION BY age) AS max_win_price , ROW_NUMBER() OVER() AS row_numbers FROM user ; 
                                        -- new column named as max_win_price containing max price of each group of rows with same age
                                        -- new column named as row_numbers containing row number of each row in the partition , 
                                        -- row_number starts from 1  

-- if over() contains any clause it will consider every single row in the partition as a single window and numbered as 1,2 for partition 1 ; 1,2 for next partition 2 , etc.

SELECT names , addr , max(price) OVER (PARTITION BY age) AS max_win_price , ROW_NUMBER() OVER(PARTITION BY age) AS row_numbers FROM user ; 

SELECT * from (SELECT Name,Occupation,ROW_NUMBER() OVER(PARTITION BY age ORDER BY Names) AS rn FROM Occupations ) x WHERE x.rn < 3;
        --  get only first 2 rows of each group of rows with same age

--   RANK() function returns the rank of the current row in the partition. rank is based on clause in over clause.

SELECT * , RANK() OVER(partition by age order by price desc) AS rank FROM users;    -- new column named as rank containing rank of each row in the partition
 
--   DENSE_RANK() function returns the rank of the current row in the partition. 
-- diff betn rank and dense_rank is that rank skip the number if duplicate entry found then rank will be like 1 ,2 ,2 , 4 
                --  but dense rank will not skip the number if duplicate entry found then ranks will be like 1 ,2 ,2 , 3





--                                 Analytical Functions 

-- LAG(col_name) function returns the value of the specified column in the row that is one row before the current row.
              -- LAG(col_name) = > 1 value lag default , LAG(col_name,2) = > 2 value lag , LAG(col_name,1,0) = > 1 value lag with default value 0 (instead of null)

SELECT * , LAG(price) OVER(PARTITION BY age ORDER BY price) AS lag_price FROM users;    -- new column named as lag_price containing lag price of each row in the partition
                                                                                        -- lag price is null if row is first in partition/group 
                                                                                        -- if not first , then it has value of previous row's price for specified column

-- LEAD(col_name) function returns the value of the specified column in the row that is one row after the current row.
            -- LEAD(col_name) = > 1 value lead default , LEAD(col_name,2) = > 2 value lead , LEAD(col_name,1,0) = > 1 value lead with default value 0 (instead of null)

SELECT * , LEAD(price) OVER(PARTITION BY age ORDER BY price) AS lead_price FROM users;    -- new column named as lead_price containing lead price of each row in the partition
                                                                                            -- lead price is null if row is last in partition/group 
                                                                                            -- if not last , then it has value of next row's price for specified column









--                         Procedures   - used so that code can be reused over and over again.  A procedure may or may not return any value

CREATE PROCEDURE GetAllUsers(name varchar(50) , age int)   -- procedure name , parameter list 
is
begin
        select * from users where name = name and age = age;
end;

EXEC GetAllUsers;    -- execute/call procedure
 
CREATE PROCEDURE GetAllUsers @addr nvarchar(30) , @age int
AS
SELECT * FROM users where addr = @addr and age = @age;    -- get all users with addr = @addr and age = @age

EXEC GetAllUsers @addr = 'pune' , @age = 20;    -- execute/call procedure


--                    Triggers 
--      trigger is a stored procedure in database which automatically invokes whenever a special event in the database occurs

-- Syntax:
-- create trigger [trigger_name] [before | after]
-- {insert | update | delete} on [table_name] [for each row]
-- [trigger_body]

CREATE OR REPLACE TRIGGER mytrigger after
insert on users for each row
declare
    id int
begin
    insert into log (name,addr) values (new.name,new.addr);
end;


--  Pivot and Unpivot are relational operators that are used to transform one table into another in order to achieve more simpler view of table.

--                        PIVOT   -> used when we want to transfer data from row level to column level 
--                        Unpivot -> operator does the opposite that is it transform the column based data into rows.

SELECT (ColumnNames) 
FROM (TableName) 
PIVOT
 ( 
   AggregateFunction(ColumnToBeAggregated)
   FOR PivotColumn IN (PivotColumnValues)
 ) AS (Alias) //Alias is a temporary name for a table




---   Complex queries

--1. retrieve all prices rounded to 2 decimal places with minimum lost_money is greter than 100

SELECT ROUND(Price,2) FROM users WHERE lost_money = (SELECT MIN(lost_money) FROM users WHERE lost_money > 100);


--2. get total occurances of name by ASC an print them as "there are total [count(name)] name"  e.g. "there are total 2 rahul"

SELECT CONCAT("there are total" , COUNT(names) , " ", names , " in the table") FROM users GROUP BY names ASC ;

--3. get total occurances of name by ASC an print them as "there are total [count(name)] name" , if count of name is greater than 1 then print "there are total [count(name)] names" 

SELECT CONCAT("there are total" , COUNT(names) , " ", names ,(IF (COUNT(*) > 1, 's',''), " in the table") FROM users GROUP BY names ASC ;

--4. use group by and order by with inner join

(SELECT CONCAT(NAME, '(', SUBSTRING(OCCUPATION, 1, 1), ')') as THETEXT FROM OCCUPATIONS)
UNION ALL 
(SELECT CONCAT('There are a total of ', COUNT(*),' ', lower(OCCUPATION), (IF (COUNT(*) > 1, 's.',''))) as THETEXTFROM OCCUPATIONS GROUP BY OCCUPATION) ORDER BY  THETEXT ASC;

SELECT (name || '(' || SUBSTR(occupation,1,1) || ')') FROM occupations ORDER BY name;
SELECT ('There are a total of ' || COUNT(occupation) || ' ' || LOWER(occupation) || 's' || '.') FROM occupations GROUP BY occupation ORDER BY COUNT(occupation), occupation ASC;







--       Normalization :  process to eliminate data redundancy and enhance data integrity in the table helps to organize the data in the database. 
        --       It is a multi-step process that sets the data into tabular form and removes the duplicated data from the relational tables.
        --      main reason for normalizing the relations is removing Insertion Anomaly ,Deletion Anomaly and Updatation Anomaly.
--  Decomposition: the process of breaking up or dividing a single relation into two or more sub relations is called as decomposition of a relation.
--  Dependency: 
--  non-prime attributes :  attributes that can not be combined with other attributes to form a composite key.
--                          in short , non-prime attributes are the attributes that can not be  part of the primary key.

--  First Normal Form :
--  A table is in first normal form if 
--      1. it has no duplicate rows i.e. atomic values
--      2. an attribute of a table cannot hold multiple values. It must hold only single-valued attribute.
        --       for this separate the records having duplicate values and store such that no duplicate records are present in the table.

--  Second Normal Form :
--  A table is in second normal form if
--      1. Obeys All rules of first normal form
--      2. all non-prime attributes are fully functional dependent on prime attributes 
--             i.e. non-prime attribute is dependent on prime attribute, which is a proper subset of the candidate key. then table is not in 2NF.

--    Third Normal Form :
--    A table is in third normal form if
--        1. Obeys All rules of second normal form
--        2.  no transitive dependency for non-prime attributes,
--        3. it does  not contain any transitive partial dependency.
        --    e.g. if A is dependent on B and B is dependent on C, but C is prime attribute, then it is not in 3NF
        --         in this case , separate A , B  and  B , C