from django.test import TestCase
from get_key.views import MIN_KEY, MAX_KEY
import json
from http import HTTPStatus as Status


class GetKeyTestCase(TestCase):
    def test_get_key(self):
        response = self.client.get('/get_key/')
        self.assertEqual(response.status_code, Status.OK)

        res = json.loads(response.content)
        self.assertEqual(len(res), 1)
        self.assertTrue(res['key'] >= MIN_KEY)
        self.assertTrue(res['key'] <= MAX_KEY)
