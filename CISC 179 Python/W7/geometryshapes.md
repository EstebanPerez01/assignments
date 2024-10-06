``` python
import math

# shapes class
class Shape:
    def area(self):
        raise NotImplementedError("Area method not implemented for shape")

# rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# square class
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

# circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# inherited exception from baseException
class InvalidValueException(BaseException):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

# Test
def main():
    try:
        rect = Rectangle(5, 10)
        print(f"Rectangle area: {rect.area()}")

        square = Square(5)
        print(f"Square area: {square.area()}")

        circle = Circle(5)
        print(f"Circle area: {circle.area()}")

        # check for positive values with assert
        assert rect.width > 0 and rect.height > 0, "Rectangle dimensions must be positive"
        assert square.width > 0, "Square side must be positive"
        assert circle.radius > 0, "Circle radius must be positive"

        # invalid value test
        invalid_shape = Rectangle(-5, 10)
        if invalid_shape.width <= 0 or invalid_shape.height <= 0:
            raise InvalidValueException("Invalid dimensions for rectangle")

    except InvalidValueException as e:
        print(f"Error: {e}")
    except AssertionError as ae:
        print(f"Assertion Error: {ae}")

if __name__ == "__main__":
    main()


```
