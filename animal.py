from main import load_settings
import random


class Animal:

    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.name = name
        self. gender = gender
        self.weight = weight

    def eat(self):
        pass

    def grow(self):
        for animal in load_settings():
            if animal['species'] == self.species:
                while self.weight <= animal['average_weight']:
                    self.weight += animal['food/weight ratio'] * self.weight

    def die(self, life_expectancy):
        chance_of_dying = self.age / life_expectancy
        for i in range(100):
            if random.random() >= chance_of_dying:
                return True
        return False
