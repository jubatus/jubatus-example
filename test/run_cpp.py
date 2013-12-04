#!/usr/bin/env python

import os
from util import pushd, run_server, run, example_root

with pushd(example_root):

    with pushd('gender'):
        with run_server('jubaclassifier', '-f', 'gender.json'):
            with pushd('cpp'):
                run('make')
                run('./gender')

    with pushd('malware_classification'):
        pass

    with pushd('movielens'):
        with run_server('jubarecommender', '-f', 'config.json'):
            with pushd('cpp'):
                run('python', 'waf', 'configure')
                run('python', 'waf')
                run('./build/ml_update')
                run('./build/ml_analysis')
