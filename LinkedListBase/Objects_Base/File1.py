class Student:
    def __init__(self):
        self.age = 0
        self.name = ""

    def display(self):
        print("My name is", self.name + ". I am", self.age, "years old")

    def say_hello(self, name):
        print(self.name, "says hello to", name)

# Main Code
s1 = Student()
s1.age = 10
s1.name = "A"
s1.display()

s2 = s1
s2.age = 20
s2.name = "B"

s2.display()
s1.display()


# My name is A. I am 10 years old
# My name is B. I am 20 years old
# My name is B. I am 20 years old

