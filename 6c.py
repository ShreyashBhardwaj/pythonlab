# Class 1
class Sportsman:
    def __init__(self, name, sport):
        self.name = name
        self.sport = sport
        print(f"Sportsman '{self.name}' plays {self.sport}")

    def show_skills(self):
        print(f"{self.name} shows great skill in {self.sport}.")

# Class 2
class Artist:
    def __init__(self, name, art_form):
        self.name = name
        self.art_form = art_form
        print(f"Artist '{self.name}' performs {self.art_form}")

    def perform(self):
        print(f"{self.name} performs beautifully in {self.art_form}.")

# Class 3 - Multiple Inheritance
class TalentedPerson(Sportsman, Artist):
    def __init__(self, name, sport, art_form):
        Sportsman.__init__(self, name, sport)
        Artist.__init__(self, name, art_form)

    def introduce(self):
        print(f"I am {self.name}, talented in both {self.sport} and {self.art_form}.")

# Main
def main():
    name = input("Enter name: ")
    sport = input("Enter sport: ")
    art = input("Enter art form: ")

    person = TalentedPerson(name, sport, art)
    person.introduce()
    person.show_skills()
    person.perform()

if __name__ == "__main__":
    main()
