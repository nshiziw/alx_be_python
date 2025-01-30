import mysql.connector

# Database connection details (replace with your own)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="alx"
)

my_cursor = mydb.cursor()

# Create a table named `customers` (if it doesn't exist)
my_cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE
)
""")

print("Table created successfully!")

# Insert some customer data
sql = "INSERT INTO customers (name, email) VALUES (%s, %s)"
val = ("John Doe", "john.doe@example.com")
my_cursor.execute(sql, val)
mydb.commit()

print(my_cursor.rowcount, "record(s) inserted.")

val = ("Jane Smith", "jane.smith@example.com")
my_cursor.execute(sql, val)
mydb.commit()

print(my_cursor.rowcount, "record(s) inserted.")

# Read all customer data
my_cursor.execute("SELECT * FROM customers")
myresult = my_cursor.fetchall()

print("Customers:")
for row in myresult:
  print(row)

# Update a customer's email
sql = "UPDATE customers SET email = %s WHERE id = %s"
val = ("updated.email@example.com", 1)
my_cursor.execute(sql, val)
mydb.commit()

print(my_cursor.rowcount, "record(s) updated.")

# Read the updated customer data
my_cursor.execute("SELECT * FROM customers WHERE id = 1")
myresult = my_cursor.fetchone()

print("Updated customer:")
print(myresult)

# Delete a customer
sql = "DELETE FROM customers WHERE id = 2"
my_cursor.execute(sql)
mydb.commit()

print(my_cursor.rowcount, "record(s) deleted.")

# Close connections
my_cursor.close()
mydb.close()

print("Database connection closed.")