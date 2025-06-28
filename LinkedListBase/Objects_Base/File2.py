class Student:
    def __init__(self):
        self.age = 0
        self.name = ""

    def display(self):
        print("My name is", self.name + ". I am", self.age, "years old")

    def say_hello(self, name):
        print(self.name, "says hello to", name)

# Main code
s1 = Student()
s1.age = 10
s1.name = "A"

s2 = Student()

temp = s1
s1 = s2
s2 = temp

s2.display()


# My name is A. I am 10 years old