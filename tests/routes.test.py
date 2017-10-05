import unittest
import sys
sys.path.append('..')
from src import server
class RoutesTest(unittest.TestCase):
    def setUp(self):
        server.app.testing = True;
        server.app.template_folder = '../templates'
        self.app = server.app.test_client()
    def test_index(self):
        root_response = self.app.get('/')
        self.assertTrue(root_response.status_code == 200)
        index_response = self.app.get('/index.html')
        self.assertTrue(index_response.status_code == 200)
        self.assertEqual(root_response.data, index_response.data)
    def test_login(self):
        login_page = self.app.get('/login.html')
        self.assertTrue(login_page.status_code == 200)
        login_response = self.app.post('/login', data=dict(username='username', password='password'))
        self.assertTrue(login_response.status_code == 200)
    def test_sign_up(self):
        sign_up_page = self.app.get('/signup.html')
        self.assertTrue(sign_up_page.status_code == 200)
        sign_up_response = self.app.post('/signup', data=dict(username='username', password='password', firstname='first', lastname='last', email='e@mail.co'))
        self.assertTrue(sign_up_response.status_code == 200)
    def test_home(self):
        pass
    def test_search(self):
        pass

if __name__ == "__main__":
    unittest.main()