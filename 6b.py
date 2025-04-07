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

# Further derived class
class Sportsman(Man):
    def __init__(self, name, age, profession, sport):
        super().__init__(name, age, profession)
        self.sport = sport
        print(f"Sportsman '{self.name}' plays {self.sport}")

    def show_skills(self):
        print(f"{self.name} demonstrates his skills in {self.sport}.")

# Main function
def main():
    print("\n=== Multilevel Inheritance ===")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    profession = input("Enter profession: ")
    sport = input("Enter sport: ")

    sportsman = Sportsman(name, age, profession, sport)
    sportsman.speak()
    sportsman.show_skills()

if __name__ == "__main__":
    main()
