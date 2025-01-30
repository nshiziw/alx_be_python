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