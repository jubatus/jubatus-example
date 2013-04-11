require 'jubatus/recommender/client'
require 'jubatus/recommender/types'

NAME = "recommender_ml"

recommender = Jubatus::Recommender::Client::Recommender.new "127.0.0.1", 9199
n = 0
for line in File.open("./dat/ml-100k/u.data", "r")
  userid, movieid, rating, mtime = line.split(' ')
  datum = Jubatus::Recommender::Datum.new [],[[movieid.to_s, rating.to_f]]
  if (n % 1000 == 0)
    p n
  end
  recommender.update_row(NAME, userid, datum)
  n = n + 1
end
