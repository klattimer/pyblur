from typing import List
import random
import numpy as np
from PIL import Image
from scipy.signal import convolve2d


def BoxBlur_random(img: Image, 
                   boxKernelDims: List[int] = [x for x in range(7, 13, 2)], 
                   **kwargs) -> Image:
    kerneldim = random.choice(boxKernelDims)
    return BoxBlur(img, kerneldim)


def BoxBlur(img: Image, dim: int) -> Image:
    imgarray = np.array(img, dtype="float32")
    kernel = BoxKernel(dim)
    convolved = np.zeros_like(imgarray, dtype = np.uint8)

    if convolved.ndim == 2:
        convolved[:, :] = convolve2d(imgarray[:, :], kernel, mode='same', fillvalue=255.0).astype("uint8")
    elif convolved.ndim == 3:    
        for i in range(convolved.shape[2]):
            convolved[:, :, i] = convolve2d(imgarray[:, :, i], kernel, mode='same', fillvalue=255.0).astype("uint8")
    else:
        raise NotImplementedError

    img = Image.fromarray(convolved)
    return img


def BoxKernel(dim: int) -> np.ndarray:
    kernelwidth = dim
    kernel = np.ones((kernelwidth, kernelwidth), dtype=np.float32)        
    normalizationFactor = np.count_nonzero(kernel)
    kernel = kernel / normalizationFactor
    return kernel