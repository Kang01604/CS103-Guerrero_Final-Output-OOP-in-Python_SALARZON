##############################################
# Q2: Build a class Employee with multiple constructors
##############################################
# This block illustrates several concepts:
#   - Encapsulation: Data (emp_id, name, department) is stored in instance attributes.
#   - Multiple Constructors: In addition to the primary __init__ constructor, two alternative
#     class methods (from_string and from_dict) provide ways to create an Employee.
#   - Static Methods: is_valid_department is defined as a static method to validate a department
#     without using any instance-specific information.
#   - Instance Methods: display_info prints the employee details.
#
# The multiple ways to construct an instance showcase the flexibility of class methods
# in providing alternate constructors for different data representations.

class Employee:
    def __init__(self, emp_id, name, department):
        # Primary constructor that initializes an Employee's attributes.
        self.emp_id = emp_id          
        self.name = name              
        self.department = department  

    @classmethod
    def from_string(cls, emp_str):
        # Alternative constructor that expects a string formatted as "emp_id-name-department".
        emp_id, name, department = emp_str.split('-')
        return cls(emp_id, name, department)

    @classmethod
    def from_dict(cls, emp_dict):
        # Alternative constructor that expects a dictionary with keys: 'emp_id', 'name', 'department'.
        return cls(emp_dict['emp_id'], emp_dict['name'], emp_dict['department'])

    @staticmethod
    def is_valid_department(department):
        # Static method to validate if the given department is one of the allowed ones.
        valid_departments = ['HR', 'IT', 'Marketing', 'Finance']
        return department in valid_departments

    def display_info(self):
        # Instance method to return a formatted string containing employee information.
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Department: {self.department}"


print("Q2: Build a class Employee with multiple constructors")
print("___________________________________________________________________")

# Using the primary constructor:
print("\nUsing __init__:")
emp1 = Employee("001", "Alice", "IT")  # Initializing using __init__
print(emp1.display_info())
print("METHOD: initialized using __init__ | Employee('001', 'Alice', 'IT')")

# Using the alternative constructor from a string:
print("\nUsing from_string:")
emp1 = Employee.from_string("001-Alice-IT")  # Reassigning emp1 using from_string
print(emp1.display_info())
print("METHOD: initialized using from_string() | Employee.from_string('001-Alice-IT')")

# Using the alternative constructor from a dictionary:
print("\nUsing from_dict:")
emp1 = Employee.from_dict({'emp_id': "001", 'name': "Alice", 'department': "IT"})  # Reassigning emp1 using from_dict
print(emp1.display_info())
print("METHOD: initialized using from_dict() | Employee.from_dict({'emp_id': '001', 'name': 'Alice', 'department': 'IT'})")

# Demonstrate the use of the static method is_valid_department:
print("\nUsing is_valid_department:")
dept_to_check = "IT"
is_valid = Employee.is_valid_department(dept_to_check)
print(f"Department '{dept_to_check}' is valid: {is_valid}")
