class Animal:
  def __init__(self, name):
    self.name = name

  def make_sound(self):
    print("Generic animal sound")

class Dog(Animal):
  def make_sound(self):
    print("Woof!")

lassie = Dog("Lassie")
lassie.make_sound()  # Output: Woof!


class Flyer:
  def fly(self):
    print("Flying...")

class Swimmer:
  def swim(self):
    print("Swimming...")

class Duck(Flyer, Swimmer):
  pass

duck = Duck()
duck.fly()  # Output: Flying...
duck.swim()  # Output: Swimming...



class Vehicle:
  def move(self):
    print("Moving...")

class Car(Vehicle):
  pass

class ElectricCar(Car):
  def charge(self):
    print("Charging...")

tesla = ElectricCar()
tesla.move()  # Output: Moving...
tesla.charge()  # Output: Charging...




class A:
    def greet(self):
        return "Hello from class A"

class B(A):
    def greet(self):
        return "Hello from class B"

class C(A):
    def greet(self):
        return "Hello from class C"

class D(B, C):
    pass

# Creating an instance of class D
obj_d = D()
print(obj_d.greet())  # Output: "Hello from class B"





class Animal:
  def make_sound(self):
    print("Generic animal sound")

class Dog(Animal):
  def make_sound(self):
    print("Woof!")

animals = [Dog(), Animal()]
for animal in animals:
  animal.make_sound()  # Output: Woof! (for Dog), Generic animal sound (for Animal)




class Duck:
    def quack(self):
        return "Duck quacks"

class Person:
    def quack(self):
        return "Person imitates duck"

# Polymorphic behavior using duck typing
def make_sound(obj):
    return obj.quack()

duck_obj = Duck()
person_obj = Person()

print(make_sound(duck_obj))    # Output: "Duck quacks
print(make_sound(person_obj))  # Output: "Person imitates duck"