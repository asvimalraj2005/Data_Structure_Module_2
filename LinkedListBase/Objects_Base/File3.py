class Student:
    def __init__(self):
        self.age = 0
        self.name = ""

    def display(self):
        print("My name is", self.name + ". I am", self.age, "years old")

    def say_hello(self, name):
        print(self.name, "says hello to", name)

# Main code
if __name__ == "__main__":
    s1 = Student()
    s1.age = 10
    s1.name = "A"

    s2 = Student()

    # Swapping ages
    temp_age = s1.age
    s1.age = s2.age
    s2.age = temp_age

    s2.display()
    
    # My name is . I am 10 years old