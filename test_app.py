import unittest
from io import BytesIO
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_upload_file_post_with_file(self):
        test_file = BytesIO(b"apple banana apple cherry apple banana cherry date date fig")

        response = self.app.post(
            '/',
            data={'file': (test_file, 'test.txt')},
            content_type='multipart/form-data'
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'apple', response.data)
        self.assertIn(b'banana', response.data)
        self.assertIn(b'cherry', response.data)

    def test_upload_file_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('<title>Анализ текста</title>', response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()