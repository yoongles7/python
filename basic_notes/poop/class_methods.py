# Class methods = allow operations related to the class itself
#                 takes "cls" as the first parameter, which represents the class itself

class Student:
    
    count = 0
    total_gpa = 0
    
    def __init__(self, name, gpa):
        self.name = name 
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
        
    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    # CLASS METHOD
    @classmethod
    def get_count(cls):
        return f"Total number of student: {cls.count}"
    
    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count:.2f}"

student1 = Student("Katsuki", 3.95)
student2 = Student("Kirishima", 3.25)
student2 = Student("Kaminari", 2.85)

print(Student.get_count())
print(Student.get_avg_gpa())