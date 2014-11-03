from animal import Animal


class Zoo:

    def __init__(self, animalsCollection, capacity, budget):
        self.animalsCollection = animalsCollection
        self.capacity = capacity
        self.budget = budget

    def see_animals(self):
        pass

    def move_to_habitat(self, species, name):
        for animal in self.animalsCollection:
            if animal.species == species and animal.name == name:
                self.animalsCollection.remove(animal)

    def accommodate(self, species, name, age, weight):
        self.new = Animal(species, age, name, weight)
        self.animalsCollection.append(self.new)
