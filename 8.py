from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        """Abstract Method: Must be implemented by subclasses"""
        pass

    def sleep(self):
        """Concrete Method: Can be used directly by subclasses"""
        print("Sleeping...")

# Concrete subclass 1
class Dog(Animal):
    def make_sound(self):
        print("Dog says: Woof!")

# Concrete subclass 2
class Cat(Animal):
    def make_sound(self):
        print("Cat says: Meow!")

# Concrete subclass 3
class Cow(Animal):
    def make_sound(self):
        print("Cow says: Moo!")

# Main execution
if __name__ == "__main__":
    # Creating objects of concrete subclasses and calling methods
    dog = Dog()
    dog.make_sound()
    dog.sleep()

    cat = Cat()
    cat.make_sound()
    cat.sleep()

    cow = Cow()
    cow.make_sound()
    cow.sleep()
