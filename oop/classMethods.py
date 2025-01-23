class Person:
    count = 0  # Class variable to count instances

    def __init__(self, name):
        self.name = name
        Person.count += 1  # Increment count on instance creation

    @classmethod
    def display_count(cls):
        print(f"Total persons created: {cls.count}")

# Usage
person1 = Person("Alice")
person2 = Person("Bob")
Person.display_count()  # Output: Total persons created: 2


class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# Usage
print(MathUtils.add(5, 3))       # Output: 8
print(MathUtils.multiply(5, 3))  # Output: 15




# Exercise

class Book:
    total_books = 0  # Class variable to count total book instances

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1  # Increment the counter when a new instance is created

    @classmethod
    def display_total_books(cls):
        return f"Total books created: {cls.total_books}"

# Demonstration
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
print(Book.display_total_books())  # Output: Total books created: 2




class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# Demonstration
print(Calculator.add(5, 3))  # Output: 8
print(Calculator.multiply(4, 6))  # Output: 24




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_child(cls, name):
        return cls(name, age=0)  # Create a new Person instance with age set to 0

# Demonstration
child = Person.create_child("Alice")
print(f"Name: {child.name}, Age: {child.age}")  # Output: Name: Alice, Age: 0
