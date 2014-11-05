import json

from zoo import *


def load_settings(file_name):
        f = open(file_name, "r")
        data = f.read()
        f.close()
        return json.loads(data)


def main():
    settings = load_settings("database.json")
    zoo = Zoo(45, 1000)
    zoo.accommodate("Lion", 9, "Ivan", "male", 140)
    zoo.accommodate("Lion", 9, "Ivanka", "female", 110)
    zoo.accommodate("Zebra", 4, "Penka", "female", 90)
    zoo.accommodate("Tiger", 5, "Rocky", "male", 130)
    zoo.accommodate("Tiger", 5, "Mariq", "female", 120)
    print(zoo.dayly_outcomes())
    zoo.animal_die("Zebra", "Penka")
    zoo.see_animals()
    zoo.born_animal(9)
    zoo.see_animals()
    #zoo.simulate()

if __name__ == '__main__':
    main()
