import json

from animal import Animal

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

    def simulate(interval_of_time, period):

