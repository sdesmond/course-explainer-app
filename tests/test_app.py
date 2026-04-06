import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Course Explainer', response.data)

    def test_index_shows_course_names(self):
        response = self.app.get('/')
        self.assertIn(b'Introduction to Python', response.data)
        self.assertIn(b'Web Development with Flask', response.data)
        self.assertIn(b'Data Science Fundamentals', response.data)
        self.assertIn(b'Go Programming Language', response.data)

    def test_course(self):
        response = self.app.get('/course/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Course Details', response.data)

    def test_course_go_lang(self):
        response = self.app.get('/course/4')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Go Programming Language', response.data)

if __name__ == '__main__':
    unittest.main()