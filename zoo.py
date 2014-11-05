from animal import *
from main import *
from random import randrange


class Zoo:

    def __init__(self, capacity, budget):
        self.animalsCollection = []
        self.capacity = capacity
        self.budget = budget
        self.animalsAfterGestationPeriod = []

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

    def born_animal(self, month):
        for animal in self.animalsCollection:
            for i in range(1, len(self.animalsCollection)):
                if animal.species == self.animalsCollection[i].species and animal.gender != self.animalsCollection[i].gender:
                    if animal in self.animalsAfterGestationPeriod or self.animalsCollection[i] in self.animalsAfterGestationPeriod:
                        continue
                    for dictionary in load_settings("database.json"):
                        if dictionary['species'] == animal.species:
                            if animal.weight < dictionary['average weight'] or self.animalsCollection[i].weight < dictionary['average weight']:
                                continue
                            if month >= dictionary['gestation period']:
                                gender = ''
                                a = randrange(100)
                                if a <= 50:
                                    gender = "male"
                                else:
                                    gender = "female"
                                print(gender)
                                self.accommodate(animal.species, 0, "Child of " + animal.name, gender, dictionary['newborn weight in kilos'])
                                if(animal.gender == "female"):
                                    self.animalsAfterGestationPeriod.append(animal)
                                else:
                                    self.animalsAfterGestationPeriod.append(self.animalsCollection[i])
        #print(self.animalsAfterGestationPeriod[0].name)


    def animal_die(self, species, name):
        for animal in self.animalsCollection:
            if animal.species == species and animal.name == name:
                self.animalsCollection.remove(animal)
                break

    def simulate(interval_of_time, period):
        pass
