#!/usr/bin/env ruby

host = "127.0.0.1"
port = 9199
name = "test"

require 'jubatus/classifier/client'
require 'jubatus/classifier/types'

client = Jubatus::Classifier::Client::Classifier.new(host, port)

train_data =
  [
   ["male",   Jubatus::Classifier::Datum.new([["hair", "short"], ["top", "sweater"], ["bottom", "jeans"]], [["height", 1.70]])],
   ["female", Jubatus::Classifier::Datum.new([["hair", "long"],  ["top", "shirt"],   ["bottom", "skirt"]], [["height", 1.56]])],
   ["male",   Jubatus::Classifier::Datum.new([["hair", "short"], ["top", "jacket"],  ["bottom", "chino"]], [["height", 1.65]])],
   ["female", Jubatus::Classifier::Datum.new([["hair", "short"], ["top", "T shirt"], ["bottom", "jeans"]], [["height", 1.72]])],
   ["male",   Jubatus::Classifier::Datum.new([["hair", "long"],  ["top", "T shirt"], ["bottom", "jeans"]], [["height", 1.82]])],
   ["female", Jubatus::Classifier::Datum.new([["hair", "long"],  ["top", "jacket"],  ["bottom", "skirt"]], [["height", 1.43]])],
#   ["male",   Jubatus::Classifier::Datum.new([["hair", "short"], ["top", "jacket"],  ["bottom", "jeans"]], [["height", 1.76]])],
#   ["female", Jubatus::Classifier::Datum.new([["hair", "long"],  ["top", "sweater"], ["bottom", "skirt"]], [["height", 1.52]])],
  ]

client.train(name, train_data)

test_data =
  [
   Jubatus::Classifier::Datum.new([["hair", "short"], ["top", "T shirt"], ["bottom", "jeans"]], [["height", 1.81]]),
   Jubatus::Classifier::Datum.new([["hair", "long"],  ["top", "shirt"],   ["bottom", "skirt"]], [["height", 1.50]]),
  ]

results = client.classify(name, test_data)

results.each { |result|
  result.each { |(label, score)|
    puts(label + " " + score.to_s)
  }
  puts
}
