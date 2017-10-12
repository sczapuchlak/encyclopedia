import unittest
from src.database import Database
from src.user import User
db = Database('sqlite:///test.sqlite3')
user = User
class DatabaseTest(unittest.TestCase):
    def test_sqlite_orm_connection(self):
        self.assertTrue(db._get_connection())
        print('Connection Working')
    def test_orm_session_connection(self):
        self.assertTrue(db._get_session())
        print('Session Working')
    def test_database_add_user_using_orm(self):
        u1 = user('test', 'er', 'tester123', 'tester@email.', 'testersSecret')
        db.add_user(u1)
        self.assertTrue(db.get_user('tester123'))
        print('Adding User Working')

if __name__ == '__main__':
    unittest.main()