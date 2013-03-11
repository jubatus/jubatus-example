#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from jubatus.recommender import client
from jubatus.recommender import types

if __name__ == '__main__':

    recommender = client.recommender("127.0.0.1",9199)

    for i in range(0,943):
        sr = recommender.similar_row_from_id("movie_len", str(i) , 10);
        print "user ", str(i),  " is similar to :", sr
  
