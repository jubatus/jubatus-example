#!/usr/bin/env python
# coding: utf-8

host = '127.0.0.1'
port = 9199
name = 'test'

import json
import random

import jubatus
from jubatus.classifier.types import datum

def train(client):
    # prepare training data
    # predict the last ones (that are commented out)
    train_data = [ 
        (u'徳川', datum([('name', u'家康')], [])),
        (u'徳川', datum([('name', u'秀忠')], [])),
        (u'徳川', datum([('name', u'家光')], [])),
        (u'徳川', datum([('name', u'家綱')], [])),
        (u'徳川', datum([('name', u'綱吉')], [])),
        (u'徳川', datum([('name', u'家宣')], [])),
        (u'徳川', datum([('name', u'家継')], [])),
        (u'徳川', datum([('name', u'吉宗')], [])),
        (u'徳川', datum([('name', u'家重')], [])),
        (u'徳川', datum([('name', u'家治')], [])),
        (u'徳川', datum([('name', u'家斉')], [])),
        (u'徳川', datum([('name', u'家慶')], [])),
        (u'徳川', datum([('name', u'家定')], [])),
        (u'徳川', datum([('name', u'家茂')], [])),
        # (u'徳川', datum([('name', u'慶喜')], [])),

        (u'足利', datum([('name', u'尊氏')], [])),
        (u'足利', datum([('name', u'義詮')], [])),
        (u'足利', datum([('name', u'義満')], [])),
        (u'足利', datum([('name', u'義持')], [])),
        (u'足利', datum([('name', u'義量')], [])),
        (u'足利', datum([('name', u'義教')], [])),
        (u'足利', datum([('name', u'義勝')], [])),
        (u'足利', datum([('name', u'義政')], [])),
        (u'足利', datum([('name', u'義尚')], [])),
        (u'足利', datum([('name', u'義稙')], [])),
        (u'足利', datum([('name', u'義澄')], [])),
        (u'足利', datum([('name', u'義稙')], [])),
        (u'足利', datum([('name', u'義晴')], [])),
        (u'足利', datum([('name', u'義輝')], [])),
        (u'足利', datum([('name', u'義栄')], [])),
        # (u'足利', datum([('name', u'義昭')], [])),

        (u'北条', datum([('name', u'時政')], [])),
        (u'北条', datum([('name', u'義時')], [])),
        (u'北条', datum([('name', u'泰時')], [])),
        (u'北条', datum([('name', u'経時')], [])),
        (u'北条', datum([('name', u'時頼')], [])),
        (u'北条', datum([('name', u'長時')], [])),
        (u'北条', datum([('name', u'政村')], [])),
        (u'北条', datum([('name', u'時宗')], [])),
        (u'北条', datum([('name', u'貞時')], [])),
        (u'北条', datum([('name', u'師時')], [])),
        (u'北条', datum([('name', u'宗宣')], [])),
        (u'北条', datum([('name', u'煕時')], [])),
        (u'北条', datum([('name', u'基時')], [])),
        (u'北条', datum([('name', u'高時')], [])),
        (u'北条', datum([('name', u'貞顕')], [])),
        # (u'北条', datum([('name', u'守時')], [])),
        ]

    # training data must be shuffled on online learning!
    random.shuffle(train_data)

    # run train
    client.train(name, train_data)

def predict(client):
    # predict the last shogun
    data = [
        datum([('name', u'慶喜')], []),
        datum([('name', u'義昭')], []),
        datum([('name', u'守時')], []),
        ]
    for d in data:
        res = client.classify(name, [d])
        # get the predicted shogun name
        print(max(res[0], key = lambda x: x.score).label, d.string_values[0][1])

if __name__ == '__main__':
    # connect to the jubatus
    client = jubatus.Classifier(host, port)
    # run example
    train(client)
    predict(client)

