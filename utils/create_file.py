from io import BytesIO


def create_file(text: str) -> BytesIO:
    img = BytesIO(bytes(text, 'utf8'))
    img.name = 'my_image.jpg'
    return img
