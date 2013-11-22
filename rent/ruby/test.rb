# -*- coding: utf-8 -*-
require 'jubatus/regression/client'
require 'readline'
require 'pp'

NAME = "a"

stty_save = `stty -g`.chomp
trap("INT") { system "stty", stty_save; exit }

status = ["面積(m^2)", "駅からの距離(分)", "築年", "階数(階)", "向き(N/NE/E/SE/S/SW/W/NW)"]

loop do
  param = status.map{|s|
    v = Readline.readline("#{s} -> ", true)
    exit(0) if v.nil?
    v
  }
  cli = Jubatus::Regression::Client::Regression.new "127.0.0.1", 9199, NAME
  data = Jubatus::Common::Datum.new("aspect" => param[4],
                                    "space" => param[0].to_f,
                                    "distance" => param[1].to_f,
                                    "age" => param[2].to_f,
                                    "stair" => param[3].to_f)
  result = cli.estimate [data]
  puts "推定家賃 #{sprintf "%.2f",result[0]} 万円/月"
  puts ""
end
