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