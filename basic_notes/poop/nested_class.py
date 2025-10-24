# Nested Class = a class defined within another class
#                class Outer:
#                   class Inner:

# Benefits: allows you to logically group classes that are closely related
#           encapsulates private details that are not relvant outside the Outer class
#           keeps the namespace clean, reduces the possibility of naming conflicts

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position
        
        def get_details(self):
            return f"{self.name} {self.position}"
     
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []
        
    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)
    
    def list_employees(self):
        return [employee.get_details() for employee in self.employees]

company1 = Company("Krusty Krab")
company2 = Company("Hero Agency")

company1.add_employee("Eugene", "Manager")
company1.add_employee("Spongebob", "Cook")
company1.add_employee("Squidward", "Cashier") 
company2.add_employee("Katsuki", "Dynamight")
company2.add_employee("Kirishima", "Red Riot") 

for employee in company1.list_employees():
    print(employee)
    
for employee in company2.list_employees():
    print(employee)