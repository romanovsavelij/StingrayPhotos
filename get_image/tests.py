from django.test import TestCase
from http import HTTPStatus as Status
from utils.get_unique_key import get_unique_key
from utils.create_file import create_file


class GetImageTestCase(TestCase):
    def setUp(self):
        self.img1 = create_file('first_image')
        self.img2 = create_file('second_image')
        self.img3 = create_file('third_image')

    def test_no_images(self):
        key = get_unique_key()

        response = self.client.post(f'/upload/?key={key}', {'images': (self.img1, self.img2, self.img3)})
        self.assertEqual(response.status_code, Status.OK)

        self.compare_image_by_key(key, self.img1)
        self.compare_image_by_key(key, self.img2)
        self.compare_image_by_key(key, self.img3)
        self.compare_image_by_key(key, self.img1)

    def test_no_key(self):
        response = self.client.get(f'/get_image/')
        self.assertEqual(response.status_code, Status.BAD_REQUEST)

    def test_multiple_uploads(self):
        key = get_unique_key()

        response = self.client.post(f'/upload/?key={key}', {'images': (self.img1, self.img2)})
        self.assertEqual(response.status_code, Status.OK)

        response = self.client.post(f'/upload/?key={key}', {'images': self.img3})
        self.assertEqual(response.status_code, Status.OK)

        self.compare_image_by_key(key, self.img1)
        self.compare_image_by_key(key, self.img2)
        self.compare_image_by_key(key, self.img3)

    def compare_image_by_key(self, key, img):
        response = self.client.get(f'/get_image/?key={key}')
        self.assertEqual(response.status_code, Status.OK)
        self.assertEqual(response.content, img.getvalue())
