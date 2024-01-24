from PIL import Image
from pyblur import RandomizedBlur, DEFAULT_BLUR_FUNCTIONS

blurFunctions = DEFAULT_BLUR_FUNCTIONS.copy()
blurFunctions["StochasticMotionBlur"]["intensity_min"] = 0.2

img = Image.open("assets/test256.png").convert("RGB")
blurred = RandomizedBlur(img, blurFunctions)
blurred.save("blurred_test.jpg")