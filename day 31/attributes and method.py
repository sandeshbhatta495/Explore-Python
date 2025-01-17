class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

# Create object
circle1 = Circle(5)
print(f"Area: {circle1.calculate_area()}")  # Output: Area: 78.5
