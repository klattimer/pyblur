"""
Source: https://github.com/LeviBorodenko/motionblur/blob/master/motionblur.py
"""
from typing import Union, List

import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from numpy.random import uniform, triangular, beta
from math import pi
from pathlib import Path
from scipy.signal import convolve
import random

from .StochasticMotionBlur_helpers import Kernel


def StochasticMotionBlur_random(img: Image, 
                                stochasticMotionBlurKernelDims: List[int] = [x for x in range(25, 35, 2)],
                                intensity: Union[float, str] = "random", 
                                **kwargs) -> Image:
    assert intensity == "random" or (isinstance(intensity, (float, int)) and intensity >= 0.0 and intensity <= 1.0), f'intensity must be "random" or a float number in range [0, 1]'
    if intensity == "random": 
        intensity = random.uniform(0.0, 1.0)
    intensity = float(intensity)
    kernelidx = np.random.randint(0, len(stochasticMotionBlurKernelDims))
    kerneldim = stochasticMotionBlurKernelDims[kernelidx]
    return StochasticMotionBlur(img, kerneldim, intensity)
    

def StochasticMotionBlur(img: Image, dim: int, intensity: float) -> Image:
    kernel = Kernel(size = (dim, dim), intensity=intensity)
    img = kernel.applyTo(img, keep_image_dim=True)
    return img

