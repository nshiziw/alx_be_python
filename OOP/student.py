class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_information(self):
        full_information = f"{self.name} {self.age}"
        return full_information

student_information = Student("Wilson", 19)
print(student_information.display_information())