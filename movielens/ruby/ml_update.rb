#!/usr/bin/env ruby

require 'jubatus/recommender/client'

NAME = "recommender_ml"

recommender = Jubatus::Recommender::Client::Recommender.new "127.0.0.1", 9199
n = 0
File.open("../dat/ml-100k/u.data", "r").each{|line|
  userid, movieid, rating, mtime = line.split(' ')
  datum = Jubatus::Recommender::Datum.new [],[[movieid.to_s, rating.to_f]]
  if (n % 1000 == 0)
    p n
  end
  recommender.update_row(NAME, userid, datum)
  n = n + 1
}
