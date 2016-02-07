import sys
from PIL import Image
from pytesseract import image_to_string
im = Image.open(sys.argv[1])
print im
print image_to_string(im)
