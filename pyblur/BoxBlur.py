import numpy as np
from PIL import Image
from scipy.signal import convolve2d

boxKernelDims = [x for x in range(9, 15, 2)]

def BoxBlur_random(img):
    kernelidx = np.random.randint(0, len(boxKernelDims))    
    kerneldim = boxKernelDims[kernelidx]
    return BoxBlur(img, kerneldim)

def BoxBlur(img, dim):
    imgarray = np.array(img, dtype="float32")
    kernel = BoxKernel(dim)
    convolved = np.zeros_like(imgarray, dtype = np.uint8)
    for i in range(3):
        convolved[:, :, i] = convolve2d(imgarray[:, :, i], kernel, mode='same', fillvalue=255.0).astype("uint8")
    img = Image.fromarray(convolved)
    return img

def BoxKernel(dim):
    kernelwidth = dim
    kernel = np.ones((kernelwidth, kernelwidth), dtype=np.float32)        
    normalizationFactor = np.count_nonzero(kernel)
    kernel = kernel / normalizationFactor
    return kernel