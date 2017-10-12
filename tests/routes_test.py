import unittest
import sys
sys.path.append('..')
from src import server
class RoutesTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('RoutesTest.setUp')
        server.app.testing = True;
        server.app.template_folder = '../templates'
        self.app = server.app.test_client()
    def test_index(self):
        print('RoutesTest.test_index')
        root_response = self.app.get('/')
        self.assertEqual(root_response.status_code, 200)
        index_response = self.app.get('/index.html')
        self.assertEqual(index_response.status_code, 200)
        self.assertEqual(root_response.data, index_response.data)
    def test_sign_up(self):
        print('RoutesTest.test_sign_up')
        sign_up_page = self.app.get('/signup.html')
        self.assertEqual(sign_up_page.status_code, 200)
        sign_up_response = self.app.post('/signup', data=dict(username='username', password='password', firstname='first', lastname='last', email='e@mail.co'))
        self.assertIn(sign_up_response.status_code, [302, 200])
    def test_sign_out(self):
        print('RoutesTest.test_sign_out')
        logout = self.app.get('/signout')
        self.assertIn(logout.status_code, [302, 200])
    def test_login(self):
        print('RoutesTest.test_login')
        login_page = self.app.get('/login.html')
        self.assertEqual(login_page.status_code, 200)
        login_response = self.app.post('/login', data=dict(username='username', password='password'))
        self.assertIn(login_response.status_code, [302, 200])
    def test_home(self):
        print('RoutesTest.test_home')
        pass
    def test_search(self):
        print('RoutesTest.test_search')
        pass
if __name__ == "__main__":
    unittest.main()