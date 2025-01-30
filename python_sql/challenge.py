import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="challenge"
)

cursor = database.cursor()

# cursor.execute("CREATE DATABASE IF NOT EXISTS challenge")

# cursor.execute("CREATE TABLE IF NOT EXISTS books (id int primary key, title varchar(255), author varchar(255), ISBN varchar(255))")

def data(title, author, ISBN):
    query = "INSERT INTO books (title, author, ISBN) VALUES (%s, %s, %s)"
    values = (title, author, ISBN)
    cursor.execute(query, values)
    database.commit()
    print(f"Book '{title}' by {author} with ISBN '{ISBN}' added successfully.")

def search(title):
    query = "SELECT * from books where title like '%s"
    values = (f"%{title}%",)
    cursor.execute(query, values)

def list_all():
    query = "SELECT * FROM books"
    cursor.execute(query)
    for row in cursor:
        print(row)

def delete_id(id):
    query = "DELETE FROM books WHERE id = %s"
    values = (id,)
    cursor.execute(query, values)
    database.commit()
    print(f"Book with ID '{id}' deleted successfully.")


data("I was never broken", "Ruth Ray", "2981")
data("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")

search("I was never")

list_all()

delete_id(1)