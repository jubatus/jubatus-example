require "jubatus/recommender/client"
require "jubatus/recommender/types"
require "pp"

recommender = Jubatus::Recommender::Client::Recommender.new "127.0.0.1", 9199

Array.new(943){|index| "#{index}"}.each{|n|
  sr = recommender.similar_row_from_id("movie_len", n.to_s, 10)
  print "user#{n} is similar to "
  sr.each{|user_tuple|
    print(" user#{user_tuple[0]} score:#{user_tuple[1]}  ")
  }
  puts ""
}
