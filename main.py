import json

from zoo import Zoo
from animal import Animal


def load_settings(file_name):
        f = open(file_name, "r")
        data = f.read()
        f.close()
        return json.loads(data)


def main():
    settings = load_settings("database.json")
    zoo = Zoo(45, 1000)
    zoo.see_animals()
    zoo.simulate()

if __name__ == '__main__':
    main()
