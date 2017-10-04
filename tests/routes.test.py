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
        index_response = self.app.get('/index.html')
        self.assertEqual(root_response, index_response)

if __name__ == "__main__":
    unittest.main()