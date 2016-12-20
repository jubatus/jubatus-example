#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from jubatus.recommender import client
from jubatus.recommender import types

if __name__ == '__main__':

    recommender = client.Recommender("127.0.0.1", 9199, 'movie_len')

    for i in range(1,943):
        sr = recommender.similar_row_from_id(str(i) , 10);
        print("user ", str(i),  " is similar to :", list(map(str, sr)))
  
