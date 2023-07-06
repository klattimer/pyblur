import numpy as np
from PIL import ImageFilter

gaussianbandwidths = [x / 2.0 for x in range(3, 15)]

def GaussianBlur_random(img):
    gaussianidx = np.random.randint(0, len(gaussianbandwidths))
    gaussianbandwidth = gaussianbandwidths[gaussianidx]
    return GaussianBlur(img, gaussianbandwidth)

def GaussianBlur(img, bandwidth):
    img = img.filter(ImageFilter.GaussianBlur(bandwidth))
    return img