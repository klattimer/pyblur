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

img = Image.open("abc.jpg")
blurred = RandomizedBlur(img)
blurred.save("test.jpg")
```
	