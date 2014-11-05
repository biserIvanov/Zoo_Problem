import random
import json


def load_settings(file_name):
        f = open(file_name, "r")
        data = f.read()
        f.close()
        return json.loads(data)


class Animal:

    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.name = name
        self. gender = gender
        self.weight = weight

    def eat(self):
        for animal in load_settings("database.json"):
            if animal['species'] == self.species:
                return animal['food/weight ratio'] * self.weight

    def feed_animal(self):
        for animal in load_settings("database.json"):
            if animal['species'] == self.species:
                if animal['food type'] == "carnivore":
                    return animal['food/weight ratio'] * self.weight * 4
                elif animal['food type'] == "herbivore":
                    return animal['food/weight ratio'] * self.weight * 2

    def grow(self):
        for animal in load_settings("database.json"):
            if animal['species'] == self.species:
                while self.weight <= animal['average_weight']:
                    self.weight += animal['food/weight ratio'] * self.weight

    def die(self):
        for animal in load_settings("database.json"):
            if animal['species'] == self.species:
                chance_of_dying = self.age / animal['life_expectancy']
            for i in range(100):
                if random.random() >= chance_of_dying:
                    return True
            return False

animal = Animal("Lion", 9, "Ivan", "male", 140)
print(animal.die())
