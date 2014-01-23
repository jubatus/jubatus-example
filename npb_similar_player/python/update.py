#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, json
from jubatus.recommender import client
from jubatus.recommender import types
from jubatus.common import Datum

NAME = "recommender_baseball";

if __name__ == '__main__':

    recommender = client.Recommender("127.0.0.1", 9199, NAME)

    for line in open('../dat/baseball.csv'):
        pname, team, bave, games, pa, atbat, hit, homerun, runsbat, stolen, bob, hbp, strikeout, sacrifice, dp, slg, obp, ops, rc27, xr27 = line[:-1].split(',')
        d = Datum({
          "チーム": team,
          "打率": float(bave),
          "試合数": float(games),
          "打席": float(pa),
          "打数": float(atbat),
          "安打": float(hit),
          "本塁打": float(homerun),
          "打点": float(runsbat),
          "盗塁": float(stolen),
          "四球": float(bob),
          "死球": float(hbp),
          "三振": float(strikeout),
          "犠打": float(sacrifice),
          "併殺打": float(dp),
          "長打率": float(slg),
          "出塁率": float(obp),
          "OPS": float(ops),
          "RC27": float(rc27),
          "XR27": float(xr27)
          })
        recommender.update_row(pname, d)
