from PIL import Image
from pyblur import RandomizedBlur, DEFAULT_BLUR_FUNCTION

blurFunctions = DEFAULT_BLUR_FUNCTION.copy()
blurFunctions["StochasticMotionBlur"]["intensity_min"] = 0.2

img = Image.open("assets/test256.png").convert("RGB")
blurred = RandomizedBlur(img, blurFunctions)
blurred.save("blurred_test.jpg")