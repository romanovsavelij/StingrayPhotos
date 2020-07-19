from django.test import TestCase
from http import HTTPStatus as Status
from utils.get_unique_key import get_unique_key
from io import BytesIO


class GetImageTestCase(TestCase):
    def test_no_images(self):
        key = get_unique_key()

        img1 = BytesIO(b'first_image')
        img1.name = 'my_image.jpg'

        img2 = BytesIO(b'second_image')
        img2.name = 'my_image.jpg'

        img3 = BytesIO(b'third_image')
        img3.name = 'my_image.jpg'

        response = self.client.post(f'/upload/?key={key}', {'images': (img1, img2, img3)})
        self.assertEqual(response.status_code, Status.OK)

        response = self.client.get(f'/get_image/?key={key}')
        self.assertEqual(response.status_code, Status.OK)
        self.assertEqual(response.content, img1.getvalue())

        response = self.client.get(f'/get_image/?key={key}')
        self.assertEqual(response.status_code, Status.OK)
        self.assertEqual(response.content, img2.getvalue())

        response = self.client.get(f'/get_image/?key={key}')
        self.assertEqual(response.status_code, Status.OK)
        self.assertEqual(response.content, img3.getvalue())

        response = self.client.get(f'/get_image/?key={key}')
        self.assertEqual(response.status_code, Status.OK)
        self.assertEqual(response.content, img1.getvalue())
