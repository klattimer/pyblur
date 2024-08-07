import random
from typing import List
import math
import numpy as np
from PIL import Image
from scipy.signal import convolve2d
from skimage.draw import line

from .LinearMotionBlur_helpers import LineDictionary


def LinearMotionBlur_random(img: Image, 
                            lineLengths: List[int] = [x for x in range(9, 25, 2)], 
                            lineTypes: List[str] = ["full", "right", "left"], 
                            **kwargs) -> Image:
    lineLength = random.choice(lineLengths)
    lineType = random.choice(lineTypes)
    lineAngle = randomAngle(lineLength)
    return LinearMotionBlur(img, lineLength, lineAngle, lineType, lineLengths)


def LinearMotionBlur(img: Image, dim: int, angle: int, linetype: str, lineLengths: List[int]) -> Image:
    imgarray = np.array(img, dtype="float32")
    kernel = LineKernel(dim, angle, linetype, lineLengths)
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


def LineKernel(dim: int, angle: int, linetype: str, lineLengths: List[int]) -> np.ndarray:
    lineDict = LineDictionary(lst_kernel_size=lineLengths)
    kernelwidth = dim
    kernelCenter = int(math.floor(dim/2))
    angle = SanitizeAngleValue(kernelCenter, angle)
    kernel = np.zeros((kernelwidth, kernelwidth), dtype=np.float32)
    lineAnchors = lineDict.lines[dim][angle]
    if(linetype == 'right'):
        lineAnchors[0] = kernelCenter
        lineAnchors[1] = kernelCenter
    if(linetype == 'left'):
        lineAnchors[2] = kernelCenter
        lineAnchors[3] = kernelCenter
    rr,cc = line(lineAnchors[0], lineAnchors[1], lineAnchors[2], lineAnchors[3])
    kernel[rr,cc]=1
    normalizationFactor = np.count_nonzero(kernel)
    kernel = kernel / normalizationFactor        
    return kernel


def SanitizeAngleValue(kernelCenter: int, angle: int) -> float:
    numDistinctLines = kernelCenter * 4
    angle = math.fmod(angle, 180.0)
    validLineAngles = np.linspace(0,180, numDistinctLines, endpoint = False)
    angle = nearestValue(angle, validLineAngles)
    return angle


def nearestValue(theta: int, validAngles: np.ndarray) -> float:
    idx = (np.abs(validAngles-theta)).argmin()
    return validAngles[idx]


def randomAngle(kerneldim: int) -> int:
    kernelCenter = int(math.floor(kerneldim/2))
    numDistinctLines = kernelCenter * 4
    validLineAngles = np.linspace(0, 180, numDistinctLines, endpoint = False)
    angle = random.choice(validLineAngles)
    return int(angle)