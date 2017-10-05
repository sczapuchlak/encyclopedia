import unittest

class TestTest(unittest.TestCase):
    def test_one(self):
        self.assertTrue(True)
    def test_two(self):
        self.assertEqual('first', 'first')
    def test_three(self):
        self.assertEqual('third', 'third')


if __name__ == '__main__':
    unittest.main()