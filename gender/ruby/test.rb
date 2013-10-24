# -*- coding: utf-8 -*-
require 'jubatus/classifier/client'
require 'readline'
require 'pp'

NAME = "a"

stty_save = `stty -g`.chomp
trap("INT") { system "stty", stty_save; exit }

status = ["hair(short/long)", "tops(shirt/sweater)", "bottom(skirt/chino)","height(m)"]

loop do
  param = status.map{|s|
    Readline.readline("#{s} -> ", true)
  }
  cli = Jubatus::Classifier::Client::Classifier.new "127.0.0.1", 9199, NAME
  data = Jubatus::Common::Datum.new(
    "hair" => param[0],
    "tops" => param[1],
    "bottom" => param[2],
    "height" => param[3].to_f)
  result = cli.classify([data])[0].max_by{|x| x.score}.label
  puts "gender would be <#{result}>"
  puts ""
end
