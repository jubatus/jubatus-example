#!/usr/bin/env ruby

require "jubatus/recommender/client"
require "pp"

recommender = Jubatus::Recommender::Client::Recommender.new "127.0.0.1", 9199, "movie_len"

Array.new(943){|index| "#{index}"}.each{|n|
  sr = recommender.similar_row_from_id(n.to_s, 10)
  print "user#{n} is similar to "
  sr.each{|user_tuple|
    print(" user#{user_tuple.id} score:#{user_tuple.score}  ")
  }
  puts ""
}
