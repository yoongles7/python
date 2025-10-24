# Static methods = method that belong to a class rather thatn any object from that class (instance)

# Instance methods = best for operations on instances of the class (objects)
# Static methods = best for utility functions that do not need to access class data 

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):        # is a static method
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions
    
employee1 = Employee("Katsuki", "Manager")
employee2 = Employee("Kirishima", "Cook")  
employee3 = Employee("Kaminari", "Cashier")

print(Employee.is_valid_position("Scientist"))      # no need to define objects to access the is_valid_position method
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())