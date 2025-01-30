import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="alx"
)


cursor = mydb.cursor()

# Create a table

cursor.execute("CREATE TABLE IF NOT EXISTS employees (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)");

# get all employees

cursor.execute("SELECT * FROM employees")

rows = cursor.fetchall()

for row in rows:
    print(row)

# insert a new employee

employee = ("John Doe", 30)

cursor.execute("INSERT INTO employees (name, age) VALUES (%s, %s)", employee)

mydb.commit()


sql = "UPDATE employees SET name = %s WHERE id = %s"
val = ("Jane", 1)
cursor.execute(sql, val)
mydb.commit() # Commit the changes

sql = "DELETE FROM employees WHERE id = %s"
val = (2,)
cursor.execute(sql, val)
mydb.commit() # Commit the changes