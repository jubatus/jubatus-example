#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2 compatibility:
from __future__ import unicode_literals

import sys
import codecs
from jubatus.recommender import client
from jubatus.recommender import types

NAME = "recommender_baseball";

if __name__ == '__main__':

    recommender = client.Recommender("127.0.0.1", 9199, NAME)

    for line in codecs.open('../dat/baseball.csv', 'r', 'utf-8'):
      pname, team, bave, games, pa, atbat, hit, homerun, runsbat, stolen, bob, hbp, strikeout, sacrifice, dp, slg, obp, ops, rc27, xr27 = line[:-1].split(',')
      sr = recommender.similar_row_from_id(pname , 4)
      print("player {0} is similar to : {0}, {1}, {2}".format(pname, sr[1].id, sr[2].id, sr[3].id))

