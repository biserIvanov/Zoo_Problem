from zoo import Settings

class Animal():
    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.name = name
        self. gender = gender
        self.weight = weight

    def eat(self):
        food_to_eat = self.FoodWeightRatio * self.weight
        self.weight += food_to_eat

    def grow(self, monthly_weight):
        while self.weight / self.age <= self.WeightAgeRatio:
            self.weight += monthly_weight

    def die(self, life_expectancy):
        chance_of_dying = self.age / life_expectancy
        return chance_of_dying
