import unittest
from zoo import Zoo


class TestZoo(unittest.TestCase):

    def setUp(self):
        self.zoo1 = Zoo(30, 2000)

    def test_accomodate(self):
        self.zoo1.accommodate("Lion", 9, "Ivan", "male", 90)
        self.assertEqual(self.zoo1.animalsCollection[0].species, "Lion")
        self.assertEqual(self.zoo1.animalsCollection[0].name, "Ivan")

if __name__ == '__main__':
    unittest.main()
