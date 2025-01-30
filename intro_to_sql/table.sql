CREATE TABLE Employees (
  EmployeeID INT PRIMARY KEY,
  FirstName VARCHAR(50) NOT NULL,
  LastName VARCHAR(50) NOT NULL,
  Email VARCHAR(100) UNIQUE,
  HireDate DATE
);


-- inserting data into table
INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, HireDate)
VALUES (1, 'John', 'Doe', 'john.doe@example.com', '2022-05-15');

INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, HireDate)
VALUES (2, 'Jane', 'Smith', 'jane.smith@example.com', '2021-08-22'),
       (3, 'Michael', 'Johnson', 'michael.johnson@example.com', '2023-02-01');


-- selecting data from table
SELECT * FROM Employees;
SELECT FirstName, LastName, Email FROM Employees;


-- create employee table
CREATE TABLE Employees (EmployeeID int PRIMARY KEY, FirstName VARCHAR(255), LastName VARCHAR(255), department VARCHAR(255), hire_date timestamp NOT NULL)

-- inserting data into the table
INSERT INTO Employees('', 'wilson', 'nshizirungu', 'ict')

-- retrieve all employees
SELECT * from Employees

CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    EnrollmentDate DATE
);

INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);


INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...),
       (value3, value4, ...),
       ...;

SELECT column1, column2, ...
FROM table_name;

SELECT FirstName, LastName, Email
FROM Students
WHERE EnrollmentDate > '2022-01-01'
ORDER BY LastName ASC;




UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;

UPDATE Students
SET Email = 'updated@example.com'
WHERE StudentID = 1;




DELETE FROM table_name
WHERE condition;

DELETE FROM Students
WHERE EnrollmentDate < '2021-01-01';


CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE NOT NULL,
    Total DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Students(StudentID)
);


INSERT INTO Orders (CustomerID, OrderDate, Total) 
VALUES 
(1, '2025-01-30', 150.75),
(2, '2025-01-30', 200.50),
(3, '2025-01-29', 99.99);


SELECT * FROM Orders WHERE OrderDate = '2025-01-30';


SELECT Orders.OrderID, Orders.OrderDate, Orders.Total, 
       Students.Name, Students.Email 
FROM Orders 
JOIN Students ON Orders.CustomerID = Students.StudentID 
WHERE Orders.CustomerID = 1;



UPDATE Orders 
SET Total = 180.00 
WHERE OrderID = 1;



DELETE FROM Orders WHERE OrderID = 3;



SELECT FirstName, LastName, Email
FROM Students
WHERE EnrollmentDate >= '2022-01-01'
ORDER BY LastName ASC;



SELECT * FROM Products ORDER BY Price ASC;


SELECT * FROM Customers WHERE City = 'New York' AND Age > 25;

SELECT * FROM Orders WHERE OrderStatus = 'Shipped' AND OrderDate > '2023-01-01';






SELECT c.Name, o.OrderID, o.OrderDate
FROM Customers c
INNER JOIN Orders o ON c.CustomerID = o.CustomerID;


SELECT Department, COUNT(*) AS EmployeeCount FROM Employees GROUP BY Department;
SELECT ProductCategory, AVG(UnitPrice) AS AvgPrice FROM Products GROUP BY ProductCategory;
SELECT OrderDate, SUM(TotalAmount) AS TotalSales FROM Orders GROUP BY OrderDate;


SELECT ProductName
FROM Products
WHERE UnitPrice > (SELECT AVG(UnitPrice) FROM Products);



CREATE ROLE StudentAdmin;
GRANT SELECT, INSERT, UPDATE, DELETE ON Students TO StudentAdmin;
CREATE USER 'admin_user' IDENTIFIED BY 'password123';
GRANT StudentAdmin TO 'admin_user';




SELECT Name, Email FROM Customers;


SELECT ProductName, Price 
FROM Products 
WHERE Price > 50;


SELECT * 
FROM Orders 
WHERE OrderDate > '2023-01-01' 
AND Status = 'Shipped';


SELECT ProductName, UnitPrice 
FROM Products 
WHERE UnitPrice > (SELECT AVG(UnitPrice) FROM Products);


SELECT Department, COUNT(*) AS TotalEmployees 
FROM Employees 
GROUP BY Department;
