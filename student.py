class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print_first_name(self):
        print(f'my first name is {self.first_name}')

class person(Student):
    def notting(self):
        print("Finish")