#!/usr/bin/env python
# -*- coding: utf-8 -*-

host = '127.0.0.1'
port = 9199
name = ''

from jubatus.burst.client import Burst
from jubatus.burst.types import *

# クライアントインスタンスを作成する
client = Burst(host, port, name)

# あらかじめキーワードを登録しておく
client.add_keyword(KeywordWithParams("バルス", 1.001, 0.1))

# それっぽいデータを生成する関数
def add(pos, burst_count, nonburst_count):
  pos = float(pos)
  client.add_documents(
    [Document(pos, "バルス!!")] * burst_count +
    [Document(pos, "ユバタス")] * nonburst_count
  )

# 適当な時系列データを生成して投入
#   Time   Burst   Non-Burst
add(   1,      5,        30)
add(  11,     15,        50)
add(  21,    500,        10)
add(  31,   2000,        10)
add(  41,  22222,        40) # バルスの高まり
add(  51,     10,        10)
add(  61,      5,        25)

# バースト検知の結果を表示
for r in client.get_result("バルス").batches:
  print(r)
