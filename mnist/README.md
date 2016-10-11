# what 
This is example for jubatus image feature plugin with mnist dataset

# requirement
**opencv 2.x** or **opencv 3.x**

# dataset
1000 mnist .jpg files (900 files for training and 100 files for test)

# task
from image files (.jpg files), estimate the handwritten numbers

# usage
## setup jubaclassifier server
```
$ jubaclassifier -f config.json&
```

## run
```
$ python jubamnist.py
```

* For the first time you use jubamnist, `mnist_jpg_1000.tar.gz` is unfold.

# Config files
[image]

set setting of the image feature extractor

- algorithm
    - Kind of image feature extractors you use.
    - **ORB**  or **RGB** is available now.
    - default : RGB
- resize 
    - decides whether you resize image file or not.
    - default : false
- x_size, y_size
    - designates image size.
    - defalt : 64