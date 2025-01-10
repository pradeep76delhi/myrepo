## test cases
import unittest
from flaskapp import app

class FlaskAppTestCase(unittest.TestCase):

    # Set up the test client for Flask
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test GET request to the homepage
    def test_homepage_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Number Operations V4", response.data)  # Check if title is in response

    # Test POST request for addition
    def test_addition_post(self):
        response = self.app.post('/', data=dict(num1='5', num2='3', operation='add'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Result: 8.0", response.data)  # Check if the result is correct

    # Test POST request for subtraction
    def test_subtraction_post(self):
        response = self.app.post('/', data=dict(num1='5', num2='3', operation='subtract'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Result: 2.0", response.data)  # Check if the result is correct

    # Test POST request with invalid numbers
    def test_invalid_input_post(self):
        response = self.app.post('/', data=dict(num1='five', num2='three', operation='add'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Please enter valid numbers", response.data)  # Check if error message is displayed

if __name__ == '__main__':
    unittest.main()
