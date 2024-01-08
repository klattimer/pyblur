from PIL import Image
from pyblur import *

img = Image.open("img.jpg")
blurred = RandomizedBlur(img)
blurred.save("test.jpg")