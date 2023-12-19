class Animal:
    def __init__(self, name, specie, family, kingdom="Animalia"):
        self.name = name
        self.specie = specie
        self.family = family
        self.kingdom = kingdom

    def make_sound(self):
        print("Grrrr...")

    def __repr__(self):
        return f"{self.specie} is a {self.family} and belongs to the {self.kingdom} kingdom."


class Cat(Animal):
    def __init__(self, name, specie, family, kingdom="Animalia"):
        super().__init__(name, specie, family, kingdom)
        self.name = "Cat"
        self.specie = "Felis catus"
        self.family = "Felidae"
        self.kingdom = "Animalia"

    def make_sound(self):
        print("Meow!")

    def __repr__(self):
        return f"{self.specie} is a {self.family} and belongs to the {self.kingdom} kingdom."

