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