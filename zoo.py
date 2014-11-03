import json

from animal import Animal
from main import load_settings



class Zoo:

    def __init__(self, capacity, budget):
        self.animalsCollection = []
        self.capacity = capacity
        self.budget = budget

    def see_animals(self):
        for animal in self.animalsCollection:
            print(animal.name + " : " + animal.species + ", " + animal.age + ", " + animal.weight)

    def move_to_habitat(self, species, name):
        for animal in self.animalsCollection:
            if animal.species == species and animal.name == name:
                self.animalsCollection.remove(animal)

    def accommodate(self, species, name, age, weight):
        self.new = Animal(species, age, name, weight)
        self.animalsCollection.append(self.new)

    def dayly_incomes(self):
        dayly = 0
        for animal in self.animalsCollection:
            dayly += 60

    def dayly_outcomes(self):
        outcomes = 0
        foodType = ""
        for animal in self.animalsCollection:
            for animal_info in load_settings():
                if animal_info['species'] == animal.species:
                    foodType = animal_info['food_type']
                    break
            if foodType == "carnivore":
                outcomes += 4
            else:
                outcomes += 2

    def animal_die(self, species, name):
        for animal in self.animalsCollection:
            if animal.species == species and animal.name == name:
                self.animalsCollection.remove(animal)
                break

    def simulate(interval_of_time, period):
        pass
