#!/usr/bin/env python

from util import pushd, run_server, run, example_root

with pushd(example_root):

    with pushd('shogun'):
        with run_server('jubaclassifier', '-f', 'shogun.json'):
            run('python', 'python/shogun.py')

    with pushd('gender'):
        with run_server('jubaclassifier', '-f', 'gender.json'):
            run('python', 'python/gender.py')

    with pushd('twitter_streaming_lang'):
        with run_server('jubaclassifier', '-f', 'twitter_streaming_lang.json'):
            pass

    with pushd('twitter_streaming_location'):
        with run_server('jubaclassifier', '-f', 'twitter_streaming_location.json'):
            pass

    with pushd('movielens'):
        with run_server('jubarecommender', '-f', 'config.json'):
            with pushd('python'):
                run('python', 'ml_update.py')
                run('python', 'ml_analysis.py')

    with pushd('npb_similar_player'):
        with run_server('jubarecommender', '-f', 'npb_similar_player.json'):
            run('python', 'python/update.py')
            run('python', 'python/analyze.py')

    with pushd('rent'):
        with run_server('jubaregression', '-f', 'rent.json'):
            run('python', 'python/jubahomes.py',
                '-t', 'dat/rent-data.csv',
                '-a', 'dat/myhome.yml')

    with pushd('train_route'):
        with run_server('jubagraph', '-f', 'train_route.json'):
            run('python', 'python/create_graph.py')
            run('python', 'python/search_route.py', '0', '144')

    with pushd('language_detection'):
        with run_server('jubaclassifier', '-f', 'space_split.json'):
            run('python', 'python/train.py')
            run('python', 'python/test.py', input='this is a pen\n\n')

    with pushd('trivial_stat'):
        with run_server('jubastat', '-f', 'stat.json'):
            with pushd('python'):
                run('python', 'stat.py')

