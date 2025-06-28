class Student:
    def __init__(self):
        self.age = 0
        self.name = None

    def display(self):
        print("My name is", self.name ,". I am", self.age, "years old")


# Main code
s1 = Student()
s1.age = 10

s2 = s1

s2.display()

#