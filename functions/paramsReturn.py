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