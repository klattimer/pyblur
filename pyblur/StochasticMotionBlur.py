"""
Source: https://github.com/LeviBorodenko/motionblur/blob/master/motionblur.py
"""
from typing import List

from PIL import Image
import random

from .StochasticMotionBlur_helpers import Kernel


def StochasticMotionBlur_random(img: Image, 
                                stochasticMotionBlurKernelDims: List[int] = [x for x in range(25, 35, 2)],
                                intensity_min: float = 0.0, 
                                intensity_max: float = 1.0, 
                                **kwargs) -> Image:
    assert intensity_min >= 0.0, f'[ERROR] "intensity_min" must be equal or above 0.0'
    assert intensity_max <= 1.0, f'[ERROR] "intensity_max" must be equal or below 1.0'
    assert intensity_min <= intensity_max, f'[ERROR] "intensity_min" must be below "intensity_max"'
    intensity = random.uniform(intensity_min, intensity_max)
    kernelidx = random.randint(0, len(stochasticMotionBlurKernelDims))
    kerneldim = random.choice(stochasticMotionBlurKernelDims)
    return StochasticMotionBlur(img, kerneldim, intensity)
    

def StochasticMotionBlur(img: Image, dim: int, intensity: float) -> Image:
    kernel = Kernel(size = (dim, dim), intensity=intensity)
    img = kernel.applyTo(img, keep_image_dim=True)
    return img

