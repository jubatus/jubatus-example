# -*- ruby coding:utf-8 -*-

require 'jubatus/regression/client'
require 'pp'

NAME = "WINE"
filename = "../winequality-white.csv"
puts "test by #{filename}"
cli = Jubatus::Regression::Client::Regression.new "127.0.0.1", 9199, NAME

num = 0
diff = 0.0

File.open(filename, "r") {|f|
  names = f.readline.split(";").map{|n| n.gsub(/"/, "").chomp.gsub(/ /, "_")}
  f.each_line {|line|
    values = line.split(";").map{|n| n.to_f}
    datum = Hash[*names.zip(values).flatten]
    quality = datum['quality']
    datum = Jubatus::Common::Datum.new(datum)
    result = cli.estimate [datum]
    # puts "#{result[0].to_i} : #{quality.to_i}\t diff: #{(result[0] - quality).abs.to_i}"
    num += 1
    diff += (result[0] - quality).abs
  }
}

puts "average #{diff / num} error"
