require "jubatus/recommender/client"
require "jubatus/recommender/types"
require "pp"

recommender = Jubatus::Recommender::Client::Recommender.new "127.0.0.1", 9199

for i in Array.new(943){|index| "#{index}"}
  sr = recommender.similar_row_from_id("movie_len", i.to_s, 10)
  pp "user #{i} is similar to : ", sr
end
