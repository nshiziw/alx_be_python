class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __del__(self):
        print(f"Goodbye, {self.name}. Object is being deleted.")

p = Person("Wilson", 20)
del p