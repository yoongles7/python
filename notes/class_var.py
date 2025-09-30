# class variables => shared among all instances of a class
#                    defined outside the constructor
#                    allows you to share data among all objects created from that class

class Student:
    
    graduation = 2025       # this is a class variable
    num_students = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1       # while modifying the class variable, we use ClassName
    
student1 = Student("Katsuki", 25)
student2 = Student("Kirishima", 24)

print(student1.name)
print(student1.age)
# print(student1.graduation)

print(student2.name)
print(student2.age)
# print(student2.graduation)
# however accessing class variable with ClassName is recommended
print(Student.graduation)
print(Student.num_students)
print(f"My graduating class of {Student.graduation} has {Student.num_students} students.")