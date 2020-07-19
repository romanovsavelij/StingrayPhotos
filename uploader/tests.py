from django.test import TestCase
from http import HTTPStatus as Status
from io import BytesIO
from utils.get_unique_key import get_unique_key
from utils.memory import TEN_MEGABYTES_IN_BYTES


class UploadTestCase(TestCase):
    def test_no_images(self):
        key = get_unique_key()

        response = self.client.get(f'/upload/?key={key}')
        self.assertEqual(response.status_code, Status.OK)
        self.assertEqual(response.context['images_exist'], False)
        self.assertEqual(len(response.context['images']), 0)

    def test_images_count(self):
        key = get_unique_key()

        img1 = BytesIO(b'my_binary_data')
        img1.name = 'my_image.jpg'

        img2 = BytesIO(b'my_binary_data')
        img2.name = 'my_image.jpg'

        response = self.client.post(f'/upload/?key={key}', {'images': (img1, img2)})
        self.assertEqual(response.status_code, Status.OK)

        response = self.client.get(f'/upload/?key={key}')
        self.assertEqual(response.status_code, Status.OK)
        self.assertEqual(response.context['images_exist'], True)
        self.assertEqual(len(response.context['images']), 2)

    def test_file_size_limit_exceeded(self):
        key = get_unique_key()

        file_bytes_count = TEN_MEGABYTES_IN_BYTES + 1
        img = BytesIO(bytes('c' * file_bytes_count, 'utf8'))
        img.name = 'big_image.jpg'

        response = self.client.post(f'/upload/?key={key}', {'images': img})
        self.assertEqual(response.status_code, Status.UNPROCESSABLE_ENTITY)

    def test_wrong_http_method(self):
        key = get_unique_key()

        response = self.client.put(f'/upload/?key={key}')
        self.assertEqual(response.status_code, Status.BAD_REQUEST)

        response = self.client.delete(f'/upload/?key={key}')
        self.assertEqual(response.status_code, Status.BAD_REQUEST)

    def test_no_key(self):
        response = self.client.get(f'/upload/')
        self.assertEqual(response.status_code, Status.BAD_REQUEST)
