from django.test import TestCase
from http import HTTPStatus as Status
from utils.get_unique_key import get_unique_key
from utils.memory import TEN_MEGABYTES_IN_BYTES
from utils.create_file import create_file


class UploadTestCase(TestCase):
    def setUp(self):
        self.img1 = create_file('first_file')
        self.img2 = create_file('second_file')

    def test_no_images(self):
        key = get_unique_key()

        response = self.client.get(f'/upload/?key={key}')
        self.assertEqual(response.status_code, Status.OK)
        self.assertEqual(response.context['images_exist'], False)
        self.assertEqual(len(response.context['images']), 0)

    def test_images_count(self):
        key = get_unique_key()

        response = self.client.post(f'/upload/?key={key}',
                                    {'images': (self.img1, self.img2)})
        self.assertEqual(response.status_code, Status.OK)

        response = self.client.get(f'/upload/?key={key}')
        self.assertEqual(response.status_code, Status.OK)
        self.assertEqual(response.context['images_exist'], True)
        self.assertEqual(len(response.context['images']), 2)

    def test_file_size_limit_exceeded(self):
        key = get_unique_key()

        file_bytes_count = TEN_MEGABYTES_IN_BYTES + 1
        big_img = create_file('c' * file_bytes_count)

        response = self.client.post(f'/upload/?key={key}', {'images': big_img})
        self.assertEqual(response.status_code, Status.UNPROCESSABLE_ENTITY)

    def test_wrong_http_method(self):
        key = get_unique_key()

        response = self.client.put(f'/upload/?key={key}', {})
        self.assertEqual(response.status_code, Status.METHOD_NOT_ALLOWED)

        response = self.client.delete(f'/upload/?key={key}')
        self.assertEqual(response.status_code, Status.METHOD_NOT_ALLOWED)

    def test_no_key(self):
        response = self.client.get(f'/upload/')
        self.assertEqual(response.status_code, Status.BAD_REQUEST)
