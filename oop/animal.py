class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"Animal {self.name} is eating"
    
    def sleep(self):
        return f"Animal {self.name} is sleeping"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        return f"Dog {self.name} is barking"
    

animal = Animal("Fox")
print(animal.eat())
print(animal.sleep())

dog = Dog("Biggy")
print(dog.eat())
print(dog.sleep())
print(dog.bark())