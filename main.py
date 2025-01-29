from extractor import Extractor
import os

image = input('Path of the image: ')

if not os.path.exists(image):
    print('File not found. Please provide a valid path.')
else:
    image_exif = Extractor(image)
    image_exif.exif()