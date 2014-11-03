import json


class Animal():
    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.name = name
        self. gender = gender
        self.weight = weight
        f = open("database.json", "r")
        data = f.read()
        jsondata = json.loads(data)
        f.close()
        for animal in jsondata:
            if animal['species'] == self.species:
                self.life_expectancy = animal['life_expectancy']
                self.food_type = animal['food_type']
                self.gestation_period = animal['gestation period']
                self.newborn_weight_kilos = animal['newborn weight in kilos']
                self.FoodWeightRatio = animal['food/weight ratio']
                self.WeightAgeRatio = animal['weight/age ratio']

    def eat(self):
            food_to_eat = self.FoodWeightRatio * self.weight
            self.weight += food_to_eat

    def grow(self, monthly_weight):
        while self.weight / self.age <= self.WeightAgeRatio:
            self.weight += monthly_weight

    def die(self, life_expectancy):
        chance_of_dying = self.age / life_expectancy
        return chance_of_dying
