from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile


def convert_to_webp(file_object: InMemoryUploadedFile, path_file_name: str):
    image = Image.open(file_object.file)
    paths = path_file_name.rfind(".")
    new_file_name = path_file_name[0:paths] + ".webp"
    image.save(new_file_name, "webp", optimize=True, quality=95)
    return True
