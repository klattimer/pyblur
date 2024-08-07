from typing import List
import random
import numpy as np
from PIL import Image
from scipy.signal import convolve2d
from skimage.draw import disk


def DefocusBlur_random(img: Image, 
                       defocusKernelDims: List[int] = [x for x in range(9, 15, 2)], 
                       **kwargs) -> Image:
    kerneldim = random.choice(defocusKernelDims)
    return DefocusBlur(img, kerneldim)


def DefocusBlur(img: Image, dim: int) -> Image:
    imgarray = np.array(img, dtype="float32")
    kernel = DiskKernel(dim)
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


def DiskKernel(dim: int) -> np.ndarray:
    kernelwidth = dim
    kernel = np.zeros((kernelwidth, kernelwidth), dtype=np.float32)
    circleCenterCoord = dim / 2
    circleRadius = circleCenterCoord# +1
    
    rr, cc = disk((circleCenterCoord, circleCenterCoord), circleRadius)
    kernel[rr,cc]=1
    
    if(dim == 3 or dim == 5):
        kernel = Adjust(kernel, dim)
        
    normalizationFactor = np.count_nonzero(kernel)
    kernel = kernel / normalizationFactor
    return kernel


def Adjust(kernel: np.ndarray, kernelwidth: int) -> np.ndarray:
    kernel[0,0] = 0
    kernel[0,kernelwidth-1]=0
    kernel[kernelwidth-1,0]=0
    kernel[kernelwidth-1, kernelwidth-1] =0 
    return kernel