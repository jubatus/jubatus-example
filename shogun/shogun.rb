#!/usr/bin/env ruby
# -*- coding: utf-8 -*-

$host = "127.0.0.1"
$port = 9199
$name = "test"

require 'json'

require 'jubatus/classifier/client'
require 'jubatus/classifier/types'

def train(client)
  # prepare training data
  # predict the last ones (that are commented out)
  train_data =
    [
     ["徳川", Jubatus::Classifier::Datum.new([["name", "家康"]], [])],
     ["徳川", Jubatus::Classifier::Datum.new([["name", "秀忠"]], [])],
     ["徳川", Jubatus::Classifier::Datum.new([["name", "家光"]], [])],
     ["徳川", Jubatus::Classifier::Datum.new([["name", "家綱"]], [])],
     ["徳川", Jubatus::Classifier::Datum.new([["name", "綱吉"]], [])],
     ["徳川", Jubatus::Classifier::Datum.new([["name", "家宣"]], [])],
     ["徳川", Jubatus::Classifier::Datum.new([["name", "家継"]], [])],
     ["徳川", Jubatus::Classifier::Datum.new([["name", "吉宗"]], [])],
     ["徳川", Jubatus::Classifier::Datum.new([["name", "家重"]], [])],
     ["徳川", Jubatus::Classifier::Datum.new([["name", "家治"]], [])],
     ["徳川", Jubatus::Classifier::Datum.new([["name", "家斉"]], [])],
     ["徳川", Jubatus::Classifier::Datum.new([["name", "家慶"]], [])],
     ["徳川", Jubatus::Classifier::Datum.new([["name", "家定"]], [])],
     ["徳川", Jubatus::Classifier::Datum.new([["name", "家茂"]], [])],
     # ["徳川", Jubatus::Classifier::Datum.new([["name", "慶喜"]], [])],

     ["足利", Jubatus::Classifier::Datum.new([["name", "尊氏"]], [])],
     ["足利", Jubatus::Classifier::Datum.new([["name", "義詮"]], [])],
     ["足利", Jubatus::Classifier::Datum.new([["name", "義満"]], [])],
     ["足利", Jubatus::Classifier::Datum.new([["name", "義持"]], [])],
     ["足利", Jubatus::Classifier::Datum.new([["name", "義量"]], [])],
     ["足利", Jubatus::Classifier::Datum.new([["name", "義教"]], [])],
     ["足利", Jubatus::Classifier::Datum.new([["name", "義勝"]], [])],
     ["足利", Jubatus::Classifier::Datum.new([["name", "義政"]], [])],
     ["足利", Jubatus::Classifier::Datum.new([["name", "義尚"]], [])],
     ["足利", Jubatus::Classifier::Datum.new([["name", "義稙"]], [])],
     ["足利", Jubatus::Classifier::Datum.new([["name", "義澄"]], [])],
     ["足利", Jubatus::Classifier::Datum.new([["name", "義稙"]], [])],
     ["足利", Jubatus::Classifier::Datum.new([["name", "義晴"]], [])],
     ["足利", Jubatus::Classifier::Datum.new([["name", "義輝"]], [])],
     ["足利", Jubatus::Classifier::Datum.new([["name", "義栄"]], [])],
     # ["足利", Jubatus::Classifier::Datum.new([["name", "義昭"]], [])],

     ["北条", Jubatus::Classifier::Datum.new([["name", "時政"]], [])],
     ["北条", Jubatus::Classifier::Datum.new([["name", "義時"]], [])],
     ["北条", Jubatus::Classifier::Datum.new([["name", "泰時"]], [])],
     ["北条", Jubatus::Classifier::Datum.new([["name", "経時"]], [])],
     ["北条", Jubatus::Classifier::Datum.new([["name", "時頼"]], [])],
     ["北条", Jubatus::Classifier::Datum.new([["name", "長時"]], [])],
     ["北条", Jubatus::Classifier::Datum.new([["name", "政村"]], [])],
     ["北条", Jubatus::Classifier::Datum.new([["name", "時宗"]], [])],
     ["北条", Jubatus::Classifier::Datum.new([["name", "貞時"]], [])],
     ["北条", Jubatus::Classifier::Datum.new([["name", "師時"]], [])],
     ["北条", Jubatus::Classifier::Datum.new([["name", "宗宣"]], [])],
     ["北条", Jubatus::Classifier::Datum.new([["name", "煕時"]], [])],
     ["北条", Jubatus::Classifier::Datum.new([["name", "基時"]], [])],
     ["北条", Jubatus::Classifier::Datum.new([["name", "高時"]], [])],
     ["北条", Jubatus::Classifier::Datum.new([["name", "貞顕"]], [])],
     # ["北条", Jubatus::Classifier::Datum.new([["name", "守時"]], [])],
    ]

  # training data must be shuffled on online learning!
  train_data.sort_by{rand}

  # run train
  client.train($name, train_data)
end

def predict(client)
  # predict the last shogun
  data =
    [
     Jubatus::Classifier::Datum.new([["name", "慶喜"]], []),
     Jubatus::Classifier::Datum.new([["name", "義昭"]], []),
     Jubatus::Classifier::Datum.new([["name", "守時"]], []),
    ]
  data.each { |d|
    res = client.classify($name, [d])
    # get the predicted shogun name
    puts res[0].max{ |x, y| x[1] <=> y[1]}[0] + d.string_values[0][1]
  }
end

# connect to the jubatus
client = Jubatus::Classifier::Client::Classifier.new($host, $port)
# run example
train(client)
predict(client)

