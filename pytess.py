from PIL import Image
from pytesseract import image_to_string
im = Image.open('asher.jpeg')
print im
print image_to_string(im)