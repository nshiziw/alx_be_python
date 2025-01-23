class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'r')     #open the file for reading

    def read_data(self):
        return self.file.read()
    
    def __del__(self):
        self.file.close()   #close the file when the object is destroyed

# create an object for fileHandler
file_obj = FileHandler('sample.txt')
print(file_obj.read_data())

# Object is no longer needed, it will be garbage collected, and __del__ method will be called automatically to close the file

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

person = Person("Alice", 30)
print(person)  # Output: Name: Alice, Age: 30


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent class constructor
        self.breed = breed

    def make_sound(self):
        print("Woof!")

dog = Dog("Buddy", "Labrador")
dog.make_sound()  # Output: Woof!

class Car:
    def __init__(self, engine):
        self.engine = engine  # Engine object as an attribute

    def start(self):
        self.engine.start()

class Engine:
    def start(self):
        print("Engine starting...")

car = Car(Engine())
car.start()  # Output: Engine starting...