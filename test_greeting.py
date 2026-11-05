import unittest
from greeting import greeting


class GreetingTests(unittest.TestCase):
    def test_named_teammate(self):
        self.assertEqual(greeting("Avery"), "Hello, Avery!")

    def test_empty_name(self):
        self.assertEqual(greeting(""), "Hello, friend!")


if __name__ == "__main__":
    unittest.main()
