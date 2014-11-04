from animal import *
from main import *


class Zoo:

    def __init__(self, capacity, budget):
        self.animalsCollection = []
        self.capacity = capacity
        self.budget = budget

    def see_animals(self):
        for animal in self.animalsCollection:
            print(animal.name + " : " + animal.species + ", " + str(animal.age) + ", " + str(animal.weight))

    def move_to_habitat(self, species, name):
        for animal in self.animalsCollection:
            if animal.species == species and animal.name == name:
                self.animalsCollection.remove(animal)

    def accommodate(self, species, age, name, gender, weight):
        if len(self.animalsCollection) < self.capacity:
            self.new = Animal(species, age, name, gender, weight)
            self.animalsCollection.append(self.new)

    def dayly_incomes(self):
        dayly = 0
        for animal in self.animalsCollection:
            dayly += 60
        return dayly

    def dayly_outcomes(self):
        outcomes = 0
        foodType = ""
        for animal in self.animalsCollection:
            foodType = ""
            for dictionary in load_settings("database.json"):
                if dictionary['species'] == animal.species:
                    foodType = dictionary["food type"]
            if foodType == "carnivore":
                outcomes += 4
            else:
                outcomes += 2
        return outcomes

    def animal_die(self, species, name):
        for animal in self.animalsCollection:
            if animal.species == species and animal.name == name:
                self.animalsCollection.remove(animal)
                break

    def simulate(interval_of_time, period):
        pass
