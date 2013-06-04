#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from jubatus.stat import client
from jubatus.stat import types

NAME = "stat_tri";

if __name__ == '__main__':

  # 1. Jubatus Serverへの接続設定
  stat = client.stat("127.0.0.1",9199)

  # 2. 学習用データの準備
  for line in open('../dat/fruit.csv'):
    fruit, diameter, weight , price = line[:-1].split(',')

    # 3. データの学習（学習モデルの更新）
    stat.push(NAME, fruit+"dia", float(diameter))
    stat.push(NAME, fruit+"wei", float(weight))
    stat.push(NAME, fruit+"pri", float(price))

  # 4. 結果の出力
  for fr in ["orange", "apple","melon"]:
    for par in ["dia","wei", "pri"]:
      print "sum :",fr+par,stat.sum(NAME, fr+par)
      print "sdv :",fr+par,stat.stddev(NAME, fr+par)
      print "max :",fr+par,stat.max(NAME, fr+par)
      print "min :",fr+par,stat.min(NAME, fr+par)
      print "ent :",fr+par,stat.entropy(NAME, fr+par)
      print "mmt :",fr+par,stat.moment(NAME,  fr+par, 1, 0.0)
