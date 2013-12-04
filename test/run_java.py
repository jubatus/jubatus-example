#!/usr/bin/env python

from util import pushd, run_server, run, example_root

with pushd(example_root):

    with pushd('shogun'):
        with run_server('jubaclassifier', '-f', 'shogun.json'):
            with pushd('java'):
                run('mvn', 'clean')
                run('sh', 'run.sh')

    with pushd('gender'):
        with run_server('jubaclassifier', '-f', 'gender.json'):
            with pushd('java'):
                run('mvn', 'clean')
                run('sh', 'run.sh')

    with pushd('twitter_streaming_location'):
        with run_server('jubaclassifier', '-f', 'twitter_streaming_location.json'):
            pass

    with pushd('movielens'):
        with run_server('jubarecommender', '-f', 'config.json'):
            with pushd('java'):
                run('mvn', 'clean')
                run('sh', 'run-update.sh')
                run('sh', 'run-analyze.sh')
