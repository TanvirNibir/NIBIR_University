class Tanvir:
    students_in_class = 0
    Graduation_year = 2024

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Tanvir.students_in_class += 1

class Brother(Tanvir):
    def __init__(self, name, age):
        super().__init__(name, age)
    def job(self):
        print("protect your brother")

class Son:
    def responsibility(self):
        print("Take care of own family")

class Student(Tanvir, Brother, Son):
    def speak(self):
        print("Hi")

# Create instances
student_1 = Student("Tanvir", 2024)
student_2 = Student("ahmed", 23)
student_3 = Student("Ayush", 28)
student_4 = Student("Tang", 30)
student_5 = Student("Hello", 29)

# Access properties and methods
print(student_1.Graduation_year)  # Output: 2024
print(student_2.students_in_class)  # Output: 5
student_5.speak()  # Output: Hi
student_4.job()  # Output: protect your brother
