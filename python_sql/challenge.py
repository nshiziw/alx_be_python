import mysql.connector

# Connect to MySQL Database
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Replace with your actual password if needed
    database="challenge"
)

cursor = database.cursor()

# Create Table (if not exists)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY, 
        title VARCHAR(255), 
        author VARCHAR(255), 
        ISBN VARCHAR(255)
    )
""")

# Function to Add Books
def add_book(title, author, ISBN):
    query = "INSERT INTO books (title, author, ISBN) VALUES (%s, %s, %s)"
    values = (title, author, ISBN)
    cursor.execute(query, values)
    database.commit()
    print(f"✅ Book '{title}' by {author} (ISBN: {ISBN}) added successfully.")

# Function to Search for a Book by Title
def search_book(title):
    query = "SELECT * FROM books WHERE title LIKE %s"
    values = (f"%{title}%",)
    cursor.execute(query, values)
    results = cursor.fetchall()

    if results:
        print("\n🔍 Search Results:")
        for row in results:
            print(f"📖 ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, ISBN: {row[3]}")
    else:
        print(f"❌ No books found with title containing '{title}'.")

# Function to List All Books
def list_all_books():
    query = "SELECT * FROM books"
    cursor.execute(query)
    results = cursor.fetchall()

    if results:
        print("\n📚 Library Books:")
        for row in results:
            print(f"📖 ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, ISBN: {row[3]}")
    else:
        print("❌ No books in the library.")

# Function to Delete a Book by ID
def delete_book(book_id):
    query = "DELETE FROM books WHERE id = %s"
    values = (book_id,)
    cursor.execute(query, values)
    database.commit()

    if cursor.rowcount > 0:
        print(f"🗑️ Book with ID {book_id} deleted successfully.")
    else:
        print(f"❌ No book found with ID {book_id}.")

# Add Sample Books
add_book("I Was Never Broken", "Ruth Ray", "2981")
add_book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")

# Search for a Book
search_book("I Was Never")

# List All Books
list_all_books()

# Delete a Book by ID
delete_book(1)

# Close the Connection
cursor.close()
database.close()
