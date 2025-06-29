class Student:
    def __init__(self):
        self.age = 0
        self.name = ""

    def display(self):
        print("My name is", self.name + ". I am", str(self.age), "years old")

    def sayHello(self, name):
        print(self.name, "says hello to", name)

def swap(s1, s2):
    tage = s1.age
    s1.age = s2.age
    s2.age = tage

    tname = s1.name
    s1.name = s2.name
    s2.name = tname

if __name__ == "__main__":
    s1 = Student()
    s1.age = 10
    s1.name = "A"

    s2 = Student()
    s2.age = 20
    s2.name = "B"

    swap(s1, s2)

    s1.display()


# My name is B. I am 20 years old

