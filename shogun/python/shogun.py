#!/usr/bin/env python
# coding: utf-8

# Python 2 compatibility:
from __future__ import unicode_literals

host = '127.0.0.1'
port = 9199
name = 'test'

import sys
import json
import random

import jubatus
from jubatus.common import Datum

def _output(unicode_value):
  if hasattr(sys.stdout, 'buffer'):
    # for Python 3
    stdout = sys.stdout.buffer
  else:
    # for Python 2
    stdout = sys.stdout
  stdout.write(unicode_value.encode('utf-8'))

def train(client):
    # prepare training data
    # predict the last ones (that are commented out)
    train_data = [
        ('徳川', Datum({'name': '家康'})),
        ('徳川', Datum({'name': '秀忠'})),
        ('徳川', Datum({'name': '家光'})),
        ('徳川', Datum({'name': '家綱'})),
        ('徳川', Datum({'name': '綱吉'})),
        ('徳川', Datum({'name': '家宣'})),
        ('徳川', Datum({'name': '家継'})),
        ('徳川', Datum({'name': '吉宗'})),
        ('徳川', Datum({'name': '家重'})),
        ('徳川', Datum({'name': '家治'})),
        ('徳川', Datum({'name': '家斉'})),
        ('徳川', Datum({'name': '家慶'})),
        ('徳川', Datum({'name': '家定'})),
        ('徳川', Datum({'name': '家茂'})),
        # (u'徳川', Datum({'name': u'慶喜'})),

        ('足利', Datum({'name': '尊氏'})),
        ('足利', Datum({'name': '義詮'})),
        ('足利', Datum({'name': '義満'})),
        ('足利', Datum({'name': '義持'})),
        ('足利', Datum({'name': '義量'})),
        ('足利', Datum({'name': '義教'})),
        ('足利', Datum({'name': '義勝'})),
        ('足利', Datum({'name': '義政'})),
        ('足利', Datum({'name': '義尚'})),
        ('足利', Datum({'name': '義稙'})),
        ('足利', Datum({'name': '義澄'})),
        ('足利', Datum({'name': '義稙'})),
        ('足利', Datum({'name': '義晴'})),
        ('足利', Datum({'name': '義輝'})),
        ('足利', Datum({'name': '義栄'})),
        # (u'足利', Datum({'name': u'義昭'})),

        ('北条', Datum({'name': '時政'})),
        ('北条', Datum({'name': '義時'})),
        ('北条', Datum({'name': '泰時'})),
        ('北条', Datum({'name': '経時'})),
        ('北条', Datum({'name': '時頼'})),
        ('北条', Datum({'name': '長時'})),
        ('北条', Datum({'name': '政村'})),
        ('北条', Datum({'name': '時宗'})),
        ('北条', Datum({'name': '貞時'})),
        ('北条', Datum({'name': '師時'})),
        ('北条', Datum({'name': '宗宣'})),
        ('北条', Datum({'name': '煕時'})),
        ('北条', Datum({'name': '基時'})),
        ('北条', Datum({'name': '高時'})),
        ('北条', Datum({'name': '貞顕'})),
        # (u'北条', Datum({'name': u'守時'})),
    ]

    # training data must be shuffled on online learning!
    random.shuffle(train_data)

    # run train
    client.train(train_data)

def predict(client):
    # predict the last shogun
    data = [
        Datum({'name': '慶喜'}),
        Datum({'name': '義昭'}),
        Datum({'name': '守時'}),
    ]
    for d in data:
        res = client.classify([d])
        # get the predicted shogun name
        shogun_name = max(res[0], key = lambda x: x.score).label
        first_name = d.string_values[0][1]
        _output('{0} {1}\n'.format(shogun_name, first_name))

if __name__ == '__main__':
    # connect to the jubatus
    client = jubatus.Classifier(host, port, name)
    # run example
    train(client)
    predict(client)

