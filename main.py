from PIL import Image
from pyblur import *

img = Image.open("assets/test256.png").convert("RGB")
blurred = RandomizedBlur(img)
blurred.save("blurred_test.jpg")