from django.test import TestCase
from django.test import Client
from get_key.views import MIN_KEY, MAX_KEY


class GetKeyTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_key(self):
        response = self.client.get('/get_key')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.content['key'] >= MIN_KEY)
        self.assertTrue(response.content['key'] <= MAX_KEY)
