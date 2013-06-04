#!/usr/bin/env ruby
# -*- coding: utf-8 -*-

HOST = "127.0.0.1"
PORT = 9199
NAME = "recommender_baseball"
require 'jubatus/recommender/client'

recommender =
  Jubatus::Recommender::Client::Recommender.new(HOST, PORT)
File.open("dat/baseball.csv") {|f|
  f.each{|line|
    pname, team, bave, games, pa, atbat, hit, homerun, runsbat,
      stolen, bob, hbp, strikeout, sacrifice, dp, slg, obp,
      ops, rc27, xr27 = line.split(",")
    sr = recommender.similar_row_from_id(NAME, pname, 4)
    puts("player #{pname} is similar to : #{sr[1][0]} #{sr[2][0]} #{sr[3][0]}")
  }
}
