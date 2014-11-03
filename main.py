import json

from zoo import Zoo


def load_settings(file_name):
        f = open(file_name, "r")
        data = f.read()
        f.close()
        return json.loads(data)


def main():
    settings = load_settings("database.json")
    zoo = zoo(45, 1000)

if __name__ == '__main__':
    main()
