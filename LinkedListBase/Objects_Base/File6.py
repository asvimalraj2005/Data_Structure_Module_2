class Student:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def display(self):
        print(f"My name is {self.name}. I am {self.age} years old")

    def say_hello(self, name):
        print(f"{self.name} says hello to {name}")

def swap(s1, s2):
    temp = s1
    s1 = s2
    s2 = temp

# Main Code
s1 = Student(10, "A")
s2 = Student(20, "B")

swap(s1, s2)

s1.display()
# My name is A. I am 10 years old
