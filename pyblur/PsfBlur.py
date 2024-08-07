# -*- coding: utf-8 -*-
import random
import numpy as np
import pickle
from PIL import Image
from scipy.signal import convolve2d
import os.path

pickledPsfFilename = os.path.join(os.path.dirname( __file__), "psf.pkl")

with open(pickledPsfFilename, 'rb') as pklfile:
    psfDictionary = pickle.load(pklfile, encoding='latin1')


def PsfBlur_random(img: Image, **kwargs) -> Image:
    psfid = random.randint(0, len(psfDictionary) - 1)
    return PsfBlur(img, psfid)
    

def PsfBlur(img: Image, psfid: int) -> Image:
    imgarray = np.array(img, dtype="float32")
    kernel = psfDictionary[psfid]
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
    
