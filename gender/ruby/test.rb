# -*- coding: utf-8 -*-
require 'jubatus/classifier/client'
require 'jubatus/classifier/types'
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
  cli = Jubatus::Classifier::Client::Classifier.new "127.0.0.1", 9199
  data = Jubatus::Classifier::Datum.new [["hair", param[0]],
                                          ["tops", param[1]],
                                          ["bottom", param[2]]],
                                        [["height", param[3].to_f]]
  result = cli.classify(NAME, [data])[0].sort{|a,b| b[1]<=>a[1]}[0][0]
  puts "gender would be <#{result}>"
  puts ""
end
