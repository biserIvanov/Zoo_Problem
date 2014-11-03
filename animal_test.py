import unittest
import animal


class AnimalTest(unittest.TestCase):
    def setUp(self):
        self.dog = animal.Animal("dog", 5, "Felix", "male", 30)

    def test_init(self):
        self.assertEqual(self.dog.name, "Felix")
        self.assertEqual(self.dog.weight, 30)

    def test_grow(self):
        self.dog.grow(10, 5)
        self.assertEqual(self.dog.weight, 40)
        self.assertEqual(self.dog.age, 10)

if __name__ == '__main__':
    unittest.main()
