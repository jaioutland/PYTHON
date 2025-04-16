'''
Pet Class
Name: Jai Outland
'''

# Define the Pet class
class Pet:
    def __init__(self, kind, breed, name):
        self.kind = kind
        self.breed = breed
        self.name = name

    def get_kind(self):
        return self.kind

    def set_kind(self, kind):
        self.kind = kind

    def get_breed(self):
        return self.breed

    def set_breed(self, breed):
        self.breed = breed

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def print_details(self):
        print(
            f"Pet Details:\n  Name: {self.name}\n  Kind: {self.kind}\n  Breed: {self.breed}")

# Conditional fun facts based on kind or breed
        if self.kind.lower() == "dog":
            if self.breed.lower() == "golden doodle":
                print("  Fun Fact: Golden Doodles are friendly and intelligent.")
            elif self.breed.lower() == "poodle":
                print("  Fun Fact: Poodles are super smart and hypoallergenic.")
            else:
                print("  Fun Fact: All dogs are loyal buddies.")
        elif self.kind.lower() == "cat":
            print("  Fun Fact: Cats are 100 percent independent.")
        elif self.kind.lower() == "snake":
            print("  Fun Fact: Snakes whisper through the grass")
        else:
            print("  Fun Fact: Every pet is family, no matter their size or species!")


pet1 = Pet("Dog", "Golden Doodle", "Sunny")
pet2 = Pet("Cat", "Siamese", "Whiskers")
pet3 = Pet("Snake", "Ball Python", "Slither")

pet1.print_details()
pet2.print_details()
pet3.print_details()

print("Special Function Demo:")
for pet in [pet1, pet2, pet3]:
    if isinstance(pet, Pet):
        print(f"{pet.name} is an instance of the Pet class.")
