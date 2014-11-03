class Animal():
    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.name = name
        self. gender = gender
        self.weight = weight

    def grow(self, weight, age):
        self.weight += weight
        self.age += age

    def eat(self):
        pass

    def die(self, life_expectancy):
        chance_of_dying = self.age / life_expectancy
        return chance_of_dying
