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
Randomly applies one of the supported blur types, with a randomized bandwidth/strenght.

``` python
from PIL import Image
from pyblur import RandomizedBlur

img = Image.open("test.jpg").convert("RGB")
blurred = RandomizedBlur(img)
blurred.save("test.jpg")
```

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