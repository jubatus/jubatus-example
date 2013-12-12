#!/usr/bin/env python

import os
from util import pushd, run, example_root

with pushd(example_root):

    with pushd('movielens'):
        if not os.path.exists('dat/ml-100k'):
            run('mkdir', '-p', 'dat')
            with pushd('dat'):
                run('wget', 'http://www.grouplens.org/system/files/ml-100k.zip')
                run('unzip', 'ml-100k.zip')
