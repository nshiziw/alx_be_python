def calculate_are(length, width):
    area = length * width
    return area

print(f"The area of a rectangle whose length is 40cm and width is 15cm is {calculate_are(40, 15)}")

def triangle_area(base, height):
    area = (base * height) / 2
    return area

b=40
h=35
print(f"The are of a triangle whose base is {b} and height is {h} is {triangle_area(b, h)}")

def user_info(name, age=None):
    """Prints user information """
    print(f"User's name is: {name}")
    if age:
        print(f"User's age is: {age}")
user_info(name="Wilson")
user_info(name="Patrick", age=45)

def default_value(name="John Doe"):
    print(f"My name is {name}")

default_value(name="Wilson")
default_value()


# return values
def retuRn(number):
    return number * number
print(f"The returned number is {retuRn(4)}")


def greetings(name):
    print(f"Hello {name}, how're you doing?")
greetings("Wilson")


def area_rectangle(length, width):
    area = length * width
    return area

print(f"Area of 30 by 12 is {area_rectangle(30, 12)}")


def check_odd_even(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

check_odd_even(33)