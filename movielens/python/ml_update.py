#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, json
from jubatus.recommender import client
from jubatus.recommender import types

NAME = "recommender_ml";

if __name__ == '__main__':

    recommender = client.Recommender("127.0.0.1", 9199, NAME)

    n = 0
    for line in open('../dat/ml-100k/u.data'):
        userid, movieid, rating, mtime = line[:-1].split('\t')
        datum = types.Datum({str(movieid): float(rating)})
        if (n % 1000 == 0):
            print n
        recommender.update_row(userid, datum)
        n = n + 1;
