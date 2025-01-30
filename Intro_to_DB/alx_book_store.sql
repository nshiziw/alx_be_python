CREATE DATABASE alx_book_store

USE alx_book_store

CREATE TABLE Books(
    book_id primary key,
    title VARCHAR(130),
    author_id foreign key(author_id) references Authors,
    price DOUBLE,
    publication_date DATE
)

CREATE TABLE Authors(
    author_id primary key,
    author_name VARCHAR(215),
)

CREATE TABLE Customers(
    customer_id PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
)

CREATE TABLE Orders(
    order_id PRIMARY KEY,
    customer_id FOREIGN KEY(customer_id) REFERENCES Customers,
    order_date DATE,
)

CREATE TABLE Order_details(
    order_detail_id PRIMARY KEY,
    order_id FOREIGN KEY(order_id) REFERENCES Orders,
    book_id FOREIGN KEY(book_id) REFERENCES Books,
    quantity DOUBLE
)