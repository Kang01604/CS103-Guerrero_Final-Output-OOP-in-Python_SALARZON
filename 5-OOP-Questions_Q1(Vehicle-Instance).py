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