# Method Overriding
class Animal:
    def speak(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("Dog barks.")

class Cat(Animal):
    def speak(self):
        print("Cat meows.")


# Operator Overloading
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        """Overloads the '+' operator to add two complex numbers."""
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        """Overloads the string representation for printing complex numbers."""
        return f"{self.real} + {self.imag}i"


# Method Overloading using default arguments
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c


# Main function
if __name__ == "__main__":
    print("=== Method Overloading ===")
    calc = Calculator()
    print("Addition of two numbers:", calc.add(10, 20))
    print("Addition of three numbers:", calc.add(10, 20, 30))

    print("\n=== Method Overriding ===")
    animal = Animal()
    dog = Dog()
    cat = Cat()
    animal.speak()
    dog.speak()
    cat.speak()

    print("\n=== Operator Overloading ===")
    c1 = ComplexNumber(2, 3)
    c2 = ComplexNumber(4, 5)
    c3 = c1 + c2
    print("Sum of complex numbers:", c3)
