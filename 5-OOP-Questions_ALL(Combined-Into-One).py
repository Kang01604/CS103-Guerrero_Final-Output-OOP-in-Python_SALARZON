##############################################
# Q1: Instance Checks for Vehicle and Non-Vehicle
##############################################
# This block demonstrates several key OOP principles:
#   - Inheritance: 'SchoolBus' is derived from 'Vehicle'
#   - Encapsulation: 'Vehicle' uses "protected" attributes (names beginning with a single underscore)
#   - Polymorphism: The __str__ method is overridden in 'SchoolBus' to provide a custom string representation.
#   - Abstraction: 'Vehicle' provides a common interface (such as start_engine) for all vehicles.
#   - Instance Checking: Using isinstance() to distinguish between objects of different classes.
#
# There is also an unrelated class 'Fruit' that is used to demonstrate that classes not
# inheriting from 'Vehicle' do not have access to its methods.
#
# Note: The commented-out line shows an example of what happens if you try to call a
# method (start_engine) on an instance that doesn’t have it, which would raise an AttributeError.

class Vehicle:
    def __init__(self, name, model):
        # Initialize the protected attributes.
        # Using a single underscore (_name, _model) signals that these should not be accessed directly.
        self._name = name      
        self._model = model    

    def __str__(self):
        # Returns a standardized string representation of a vehicle.
        return f"Vehicle({self.name}, {self._model})"

    def start_engine(self):
        # Simulates the action of starting the vehicle's engine.
        return "Engine started."

class SchoolBus(Vehicle):
    def __init__(self, name, model, capacity):
        # Call the parent constructor to initialize shared attributes: name and model.
        super().__init__(name, model)
        # Set the additional attribute unique to SchoolBus (its seating capacity).
        self.capacity = capacity

    def __str__(self):
        # Overrides the parent's __str__ method to include capacity information.
        return f"INFO: {self._name} School Bus, made in {self._model}, with a capacity of {self.capacity} passengers."

# Unrelated class that does not derive from Vehicle.
class Fruit:
    def __init__(self, name, color):
        # Standard initialization for a Fruit; no relation to Vehicle.
        self.name = name
        self.color = color

    def __str__(self):
        # Provides a custom string representation for a Fruit.
        return f"INFO: {self.color} {self.name}"

# --- Q1 OUTPUT ---
print("\nQ1: Determine if School bus is also an instance of the Vehicle class")
print("___________________________________________________________________")
print("------ Testing with a Vehicle instance ------")
bus = SchoolBus("Mitsubishi L300XV", "2014", 17)  # Create a SchoolBus instance.
print(bus.start_engine())  # Inherited method from Vehicle demonstrating abstraction.
print(bus)                 # Demonstrates polymorphism: the overridden __str__ method is called.
print(f"Is {bus._name} School Bus an instance of Vehicle?", isinstance(bus, Vehicle))

print("\n------ Testing with a Non-Vehicle instance ------")
fruit = Fruit("Apple", "Red")  # Create a Fruit instance.
print(fruit)                   # Uses its own __str__ method from the Fruit class.
print(f"Is {fruit.name} an instance of Vehicle?", isinstance(fruit, Vehicle))

# Uncommenting the next line would raise an AttributeError because 'fruit'
# does not have a start_engine method (since it is not a Vehicle).
# print(fruit.start_engine())

print("\n==================================================================\n")

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

print("\n==================================================================\n")

##############################################
# Q3: Build two classes SchoolOne and SchoolTwo that display students' average grades and GPA.
##############################################
# Here we introduce:
#   - Abstraction: The 'School' class is an abstract base class (using ABC) which defines a template.
#   - Inheritance: 'SchoolOne' and 'SchoolTwo' inherit from 'School' and must implement the abstract methods.
#   - Encapsulation: The student grades are stored in a protected attribute (_students).
#   - Aggregation: Each school contains a list of student grades.
#   - Nested Class: 'GradeCalculator' is a nested helper class providing static methods to calculate average and GPA.
#
# This design ensures that every subclass of School implements its own methods for calculating
# the average and GPA while reusing the common display logic provided in display_stats().

from abc import ABC, abstractmethod  # Import abstract class support

class School(ABC):
    def __init__(self, name, students):
        # 'name' is public; 'students' (a list of grades) is protected.
        self.name = name            
        self._students = students   

    @abstractmethod
    def calculate_average(self):
        # Abstract method to compute the average of students' grades.
        pass

    @abstractmethod
    def calculate_gpa(self):
        # Abstract method to compute the GPA based on a specific scale.
        pass

    # Nested class that provides helper methods for grade calculations.
    class GradeCalculator:
        @staticmethod
        def average(grades):
            return sum(grades) / len(grades) if grades else 0

        @staticmethod
        def gpa(grades, scale):
            avg = School.GradeCalculator.average(grades)
            # Convert the average grade to a GPA using a provided scale divisor.
            return round(avg / scale, 2)

    def display_stats(self):
        # Display statistics if student data is available.
        if not self._students:
            print(f"{self.__class__.__name__} - {self.name}: No student data available.\n")
            return

        # Print out each student's grade.
        print(f"{self.__class__.__name__} | {self.name} Student Grades:")
        for idx, grade in enumerate(self._students, start=1):
            print(f"  Student {idx}: {grade}")

        # Compute and show details of the average calculation.
        total = sum(self._students)
        count = len(self._students)
        avg = self.calculate_average()
        print("\n  -- Average Calculation Breakdown --")
        print(f"     Sum of grades = {total}")
        print(f"     Number of students = {count}")
        print(f"     Average = {total} / {count} = {avg:.2f}")

        # Compute and show details of the GPA calculation.
        gpa = self.calculate_gpa()
        scale = getattr(self, 'gpa_scale', None)
        print("\n  -- GPA Calculation Breakdown --")
        print(f"     Scale divisor = {scale}")
        print(f"     GPA = {avg:.2f} / {scale} = {gpa:.2f}\n")

# SchoolOne uses a specific GPA scale divisor.
class SchoolOne(School):
    gpa_scale = 25  # Defines the divisor for converting average grade to GPA.

    def calculate_average(self):
        # Uses the nested GradeCalculator to compute the average.
        return self.GradeCalculator.average(self._students)

    def calculate_gpa(self):
        # Uses the nested GradeCalculator with SchoolOne's GPA scale.
        return self.GradeCalculator.gpa(self._students, self.gpa_scale)

# SchoolTwo with a different GPA scale.
class SchoolTwo(School):
    gpa_scale = 20  # This scale is different, simulating a different grading system.

    def calculate_average(self):
        return self.GradeCalculator.average(self._students)

    def calculate_gpa(self):
        return self.GradeCalculator.gpa(self._students, self.gpa_scale)

# --- Q3 OUTPUT ---
print("Q3: Build a two class call SchoolOne and SchoolTwo that")
print("    display there list of students average grades and GPA.")
print("___________________________________________________________________")
school_one = SchoolOne("Greenwood High", [88, 92, 79, 85, 91])
school_two = SchoolTwo("Maple Leaf School", [75, 84, 90, 68, 82])

school_one.display_stats()
school_two.display_stats()

print("==================================================================\n")

##############################################
# Q4: Operator Overloading - Create a Vector class that supports addition using the + operator.
##############################################
# In this block:
#   - Encapsulation is enforced via private attributes (__x and __y).
#   - The __add__ method is overloaded to allow adding two Vector instances.
#   - The __repr__ method is provided for an unambiguous representation of the vector.
#   - A static method (dot_product) computes the dot product of two vectors.
#   - A class method (origin) is provided as a factory for a vector at the origin.
#
# If an operand that is not a Vector is provided during addition, the code raises a TypeError,
# ensuring type safety.

class Vector:
    def __init__(self, x, y):
        # Private attributes: prepending with __ makes them name-mangled.
        self.__x = x  
        self.__y = y  

    def __add__(self, other):
        # Overload the '+' operator.
        if isinstance(other, Vector):
            # Create and return a new Vector with each corresponding component added together.
            return Vector(self.__x + other.__x, self.__y + other.__y)
        # If 'other' is not a Vector, raise an error.
        raise TypeError("Operand must be of type Vector")

    def __repr__(self):
        # Provide a clear representation of the vector for debugging.
        return f"Vector({self.__x}, {self.__y})"

    @staticmethod
    def dot_product(v1, v2):
        # Calculate the dot product from two vectors using their private attributes.
        return v1.__x * v2.__x + v1.__y * v2.__y

    @classmethod
    def origin(cls):
        # Return a new Vector instance at the origin (0,0).
        return cls(0, 0)

# --- Q4 OUTPUT ---
print("Q4: Operator Overloading Create a Vector class that supports addition")
print("    using the + operator, allowing you to add two vectors.")
print("___________________________________________________________________")
vector1 = Vector(5, 6)    # Creating the first vector.
vector2 = Vector(7, 8)  # Creating the second vector.
vector3 = vector1 + vector2  # Using the overloaded addition operator.

print(f"vector1: {vector1}")
print(f"vector2: {vector2}")
print(f"\nvector1 + vector2 = {vector3}")

# Demonstrate the dot product static method.
print("\nDot Product of vector1 and vector2:", Vector.dot_product(vector1, vector2))

# Demonstrate the class method for obtaining a vector at the origin.
print("\nOrigin vector:", Vector.origin())

# Testing error handling with non-Vector input.
print("\n------ Q4: Testing with non-Vector input ------")
try:
    # This should fail because 5 is not a Vector.
    result = vector1 + 5
except TypeError as error:
    print("ERROR:", error)

print("\n==================================================================\n")

##############################################
# Q5: Composition Over Inheritance - Create a Book class with an Author class included within it.
##############################################
# This block illustrates composition and aggregation:
#   - Composition: A Book is composed of an Author (the Book "has an" Author).
#   - Aggregation: A Book aggregates Chapters (kept as a list).
#   - Nested Class: Chapter is defined within the Book class to logically group it.
#   - Encapsulation: Each class has clearly defined responsibilities and data members.
#
# This design shows how to build complex objects by composing simpler ones,
# thereby favoring flexible design over deep inheritance hierarchies.

class Author:
    def __init__(self, name):
        # The Author’s name is stored as a public attribute.
        self.name = name  

    def __str__(self):
        # Returns a string representation for the author.
        return f"Author: {self.name}"


class Book:
    # Nested Chapter class to represent individual chapters.
    class Chapter:
        def __init__(self, title, num_pages):
            self.title = title          # The chapter’s title.
            self.num_pages = num_pages  # The number of pages in the chapter.

        def __str__(self):
            # Returns a string showing the chapter title and its page count.
            return f"{self.title} ({self.num_pages} pages)"

    def __init__(self, title, author: Author, chapters=None):
        # Initialize the Book with a title and an Author object.
        self.title = title      
        self.author = author    # Composition: the Book directly includes an Author instance.
        # Aggregation: the Book holds a list of chapters.
        self.chapters = chapters if chapters is not None else []

    def add_chapter(self, chapter: 'Book.Chapter'):
        # Adds a chapter to the book’s chapter list.
        self.chapters.append(chapter)

    def __str__(self):
        # Provides a full description of the book including a numbered listing of chapters.
        chapter_details = "\n  ".join(
            f"Chapter {i + 1}: {chapter}" for i, chapter in enumerate(self.chapters)
        )
        return f"Book: {self.title}\n{self.author}\nChapters:\n  {chapter_details}"

# --- Q5 OUTPUT ---
print("Q5: Composition Over Inheritance: Create a Book class with a Author class")
print("    included within it, demonstrating composition over inheritance.")
print("___________________________________________________________________")
# Create an Author instance.
author = Author("Koyoharu Gotouge")
# Create a Book instance, here representing Volume 1 of a manga.
book = Book("Kimetsu no Yaiba: Volume 1", author)

# Add chapters to the book along with their page counts.
book.add_chapter(Book.Chapter("Cruelty", 55))
book.add_chapter(Book.Chapter("The Stranger", 25))
book.add_chapter(Book.Chapter("Return by Dawn", 23))
book.add_chapter(Book.Chapter("Tanjiro's Journal, Part One", 19))
book.add_chapter(Book.Chapter("Tanjiro's Journal, Part Two", 19))
book.add_chapter(Book.Chapter("A Mountain of Hands", 19))
book.add_chapter(Book.Chapter("Spirits of the Deceased", 21))

print(book)

print("\n==================================================================")