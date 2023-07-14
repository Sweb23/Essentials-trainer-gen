import random


class TrType:
    def __init__(self,ID,gender=None,preferredTypes=[]):
        self.ID = ID
        self.gender = gender
        self.preferredTypes = preferredTypes
        
    def __str__(self):
        return f"[{self.ID}] -- {self.gender} -- {self.preferredTypes}"
        
MaleNames = ["Harley", "Joseph", "Arthur", "Kai", "Russell", "Dexter", "Dominick", "Joey", "Nico", "Carson", "Channing",
             "Casper", "Cameron", "Rory",
             "Marco", "Bradley"]
FemaleNames = ["Ellie", "Eleanor", "Poppy", "Daisy", "Lana", "Melissa", "Riley", "Elena", "Olivia", "Sydney", "Alice",
               "Annie", "Melody", "Vanessa",
               "Autumn"]



class IndividualTrainer:
    def __init__(self,type):
        self.type = type
        if type.gender == "M":
            self.name = random.choice(MaleNames)
        elif type.gender == "F":
            self.name = random.choice(FemaleNames)
        else:
            self.name = random.choice(MaleNames) + " & " + random.choice(FemaleNames)
        
    