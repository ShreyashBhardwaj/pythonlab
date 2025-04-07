# Base class
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Human created: {self.name}, Age: {self.age}")

    def speak(self):
        print(f"{self.name} can speak.")

# Derived class
class Man(Human):
    def __init__(self, name, age, profession):
        super().__init__(name, age)  # Call Human constructor
        self.profession = profession
        print(f"Man '{self.name}' works as a {self.profession}")

    def speak(self):  # Overriding the method
        print(f"{self.name}, the man, is speaking about {self.profession}.")

# Main function
def main():
    print("\n=== Single Inheritance ===")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    profession = input("Enter profession: ")

    man = Man(name, age, profession)
    man.speak()

if __name__ == "__main__":
    main()
