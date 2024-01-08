import random
from .BoxBlur import BoxBlur_random
from .DefocusBlur import  DefocusBlur_random
from .GaussianBlur import GaussianBlur_random
from .LinearMotionBlur import LinearMotionBlur_random
from .PsfBlur import PsfBlur_random
from .StochasticMotionBlur import StochasticMotionBlur_random

blurFunctions = {
    "0": {
        "func": BoxBlur_random,
        "prob": 1,
        "kwargs": {
            "boxKernelDims": [x for x in range(9, 15, 2)]
        }
    },
    "1": {
        "func": DefocusBlur_random,
        "prob": 1,
        "kwargs": {
            "defocusKernelDims": [x for x in range(9, 15, 2)]
        } 
    },
    "2": {
        "func": GaussianBlur_random,
        "prob": 1,
        "kwargs": {
            "gaussianbandwidths": [x / 2.0 for x in range(3, 11)]
        }
    },
    "3": {
        "func": LinearMotionBlur_random,
        "prob": 1,
        "kwargs": {
            "lineLengths": [x for x in range(9, 15, 2)],
            "lineTypes": ["full", "right", "left"]
        }
    },
    "4": {
        "func": PsfBlur_random,
        "prob": 1,
        "kwargs": {}
    },
    "5": {
        "func": StochasticMotionBlur_random,
        "prob": 3,
        "kwargs": {
            "stochasticMotionBlurKernelDims": [x for x in range(25, 35, 2)],
            "intensity_min": 0.0, # a float number in range [0.0, 1.0]
            "intensity_max": 1.0  # a float number in range [0.0, 1.0]
        }
    },
}


def RandomizedBlur(img):
    random_func = list(blurFunctions.keys())
    random_weights = [blurFunctions[x]["prob"] for x in blurFunctions.keys()]
    selected_func = random.choices(random_func, weights=random_weights, k=1)[0]
    blurToApply = blurFunctions[str(selected_func)]
    blurFunc = blurToApply["func"]
    kwargs = blurToApply["kwargs"]
    print(blurFunc)
    return blurFunc(img, **kwargs)