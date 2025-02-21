from typing import List
import random
from PIL import ImageFilter
from PIL import Image

def GaussianBlur_random(img: Image, 
                        gaussianbandwidths: List[float] = [x / 2.0 for x in range(3, 11)], 
                        **kwargs) -> Image:
    gaussianbandwidth = random.choice(gaussianbandwidths)
    return GaussianBlur(img, gaussianbandwidth)

def GaussianBlur(img: Image, bandwidth: float) -> Image:
    img = img.filter(ImageFilter.GaussianBlur(bandwidth))
    return img