# Modified Pyblur

Modify function of Pyblur, also add StochasticMotionBlur

## Installation

From pip: `pip install git+https://github.com/PD-Mera/pyblur.git`

Or alternatively `git clone` this repo and run locally

``` bash
git clone https://github.com/PD-Mera/pyblur.git
pip install -e pyblur
```

## Usage

### Random Blur
Randomly applies one of the supported blur types, with a randomized bandwidth/strengh.

``` python
from PIL import Image
from pyblur import RandomizedBlur

img = Image.open("test.jpg").convert("RGB")
blurred = RandomizedBlur(img)
blurred.save("test.jpg")
```

or you can modify DEFAULT_BLUR_FUNCTIONS to randomize with your own config

``` python
from PIL import Image
from pyblur import RandomizedBlur, DEFAULT_BLUR_FUNCTIONS

# print(DEFAULT_BLUR_FUNCTIONS) # Using if you want to see more config
blurFunctions = DEFAULT_BLUR_FUNCTIONS.copy()
blurFunctions["StochasticMotionBlur"]["intensity_min"] = 0.2

img = Image.open("test.jpg").convert("RGB")
blurred = RandomizedBlur(img, blurFunctions)
blurred.save("test.jpg")
```

<details>
  <summary>Click here to view default config</summary>

``` python
DEFAULT_BLUR_FUNCTIONS = {
    "BoxBlur": {
        "func": BoxBlur_random,
        "prob": 1,
        "kwargs": {
            "boxKernelDims": [x for x in range(9, 15, 2)]
        }
    },
    "DefocusBlur": {
        "func": DefocusBlur_random,
        "prob": 1,
        "kwargs": {
            "defocusKernelDims": [x for x in range(9, 15, 2)]
        } 
    },
    "GaussianBlur": {
        "func": GaussianBlur_random,
        "prob": 1,
        "kwargs": {
            "gaussianbandwidths": [x / 2.0 for x in range(3, 11)]
        }
    },
    "LinearMotionBlur": {
        "func": LinearMotionBlur_random,
        "prob": 1,
        "kwargs": {
            "lineLengths": [x for x in range(9, 15, 2)],
            "lineTypes": ["full", "right", "left"]
        }
    },
    "PsfBlur": {
        "func": PsfBlur_random,
        "prob": 1,
        "kwargs": {}
    },
    "StochasticMotionBlur": {
        "func": StochasticMotionBlur_random,
        "prob": 3,
        "kwargs": {
            "stochasticMotionBlurKernelDims": [x for x in range(25, 35, 2)],
            "intensity_min": 0.0, # a float number in range [0.0, 1.0]
            "intensity_max": 1.0  # a float number in range [0.0, 1.0]
        }
    },
}
```

</details>

## Example

<details>
  <summary>Click here to view example</summary>

| High Quality |
| :---: |
| ![](./assets/test256.png) |

| Box Blur | Defocus Blur |
| :---: | :---: |
| ![](./assets/box_blur.jpg) | ![](./assets/defocus_blur.jpg) |

| Gaussian Blur | Linear Motion Blur |
| :---: | :---: |
| ![](./assets/gaussian_blur.jpg) | ![](./assets/linear_motion_blur.jpg) |

| Psf Blur | Stochastic Motion Blur |
| :---: | :---: |
| ![](./assets/psf_blur.jpg) | ![](./assets/stochastic_motion_blur.jpg) |

</details>

## Reference

- [lospooky/pyblur](https://github.com/lospooky/pyblur)
- [LeviBorodenko/motionblur](https://github.com/LeviBorodenko/motionblur)