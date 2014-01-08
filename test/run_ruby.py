#!/usr/bin/env python

from util import pushd, run_server, run, example_root

with pushd(example_root):

    with pushd('shogun'):
        with run_server('jubaclassifier', '-f', 'shogun.json'):
            run('ruby', 'ruby/shogun.rb')

    with pushd('gender'):
        with run_server('jubaclassifier', '-f', 'gender.json'):
            run('ruby', 'ruby/gender.rb')

    with pushd('movielens'):
        with run_server('jubarecommender', '-f', 'config.json'):
            with pushd('ruby'):
                run('ruby', 'ml_update.rb')
                run('ruby', 'ml_analysis.rb')

    with pushd('npb_similar_player'):
        with run_server('jubarecommender', '-f', 'npb_similar_player.json'):
            run('ruby', 'ruby/update.rb')
            run('ruby', 'ruby/analyze.rb')

    with pushd('rent'):
        with run_server('jubaregression', '-f', 'rent.json'):
            run('ruby', 'ruby/train.rb', 'dat/rent-data.csv')
            run('ruby', 'ruby/test.rb', input='19.9\n2\n22\n4\nW\n')

    with pushd('language_detection'):
        with run_server('jubaclassifier', '-f', 'space_split.json'):
            run('ruby', 'ruby/train.rb')
            run('ruby', 'ruby/test.rb', input='this is a pen\n\n')
