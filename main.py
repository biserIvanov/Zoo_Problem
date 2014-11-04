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
    zoo.accommodate("Lion", 9, "Ivan", "male", 90)
    zoo.accommodate("Lion", 9, "Ivanka", "female", 80)
    zoo.accommodate("Zebra", 4, "Penka", "female", 90)
    zoo.accommodate("Tiger", 5, "Rocky", "male", 100)
    zoo.see_animals()
    print(zoo.dayly_outcomes())
    zoo.animal_die("Zebra", "Penka")
    zoo.move_to_habitat("Tiger", "Rocky")
    zoo.see_animals()
    #zoo.simulate()

if __name__ == '__main__':
    main()
