#!/usr/bin/env ruby

host = "127.0.0.1"
port = 9199
name = "test"

require 'jubatus/classifier/client'
require 'jubatus/classifier/types'

client = Jubatus::Classifier::Client::Classifier.new(host, port, name)

train_data =
  [
   ["male",   Jubatus::Common::Datum.new({"hair" => "short", "top" => "sweater", "bottom" => "jeans", "height" => 1.70})],
   ["female", Jubatus::Common::Datum.new({"hair" => "long",  "top" => "shirt",   "bottom" => "skirt", "height" => 1.56})],
   ["male",   Jubatus::Common::Datum.new({"hair" => "short", "top" => "jacket",  "bottom" => "chino", "height" => 1.65})],
   ["female", Jubatus::Common::Datum.new({"hair" => "short", "top" => "T shirt", "bottom" => "jeans", "height" => 1.72})],
   ["male",   Jubatus::Common::Datum.new({"hair" => "long",  "top" => "T shirt", "bottom" => "jeans", "height" => 1.82})],
   ["female", Jubatus::Common::Datum.new({"hair" => "long",  "top" => "jacket",  "bottom" => "skirt", "height" => 1.43})],
#   ["male",   Jubatus::Common::Datum.new({"hair" => "short", "top" => "jacket",  "bottom" => "jeans", "height" => 1.76})],
#   ["female", Jubatus::Common::Datum.new({"hair" => "long",  "top" => "sweater", "bottom" => "skirt", "height" => 1.52})],
  ]

client.train(train_data)

test_data =
  [
   Jubatus::Common::Datum.new({"hair" => "short", "top" => "T shirt", "bottom" => "jeans", "height" => 1.81}),
   Jubatus::Common::Datum.new({"hair" => "long",  "top" => "shirt",   "bottom" => "skirt", "height" => 1.50}),
  ]

results = client.classify(test_data)

results.each { |result|
  result.each { |r|
    puts(r.label + " " + r.score.to_s)
  }
  puts
}
