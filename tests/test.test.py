import unittest
from src.login import UserManager

def test_add_user():
    name = UserManager.add_user()
    assert name == "test"

class TestTest(unittest.TestCase):
    def first_test(self):
        assert(True)
    def second_test(self):
        assertEqual('first', 'first')
    def second_test(self):
        assertEqual('third', 'third')


if __name__ == '__main__':
    unittest.main()