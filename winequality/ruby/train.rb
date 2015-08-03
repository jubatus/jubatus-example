# -*- ruby coding:utf-8 -*-

require 'jubatus/regression/client'
require 'pp'

NAME = "WINE"
filename = "../winequality-white.csv"
puts "train by #{filename}"

cli = Jubatus::Regression::Client::Regression.new "127.0.0.1", 9199, NAME
File.open(filename, "r") {|f|
  names = f.readline.split(";").map{|n| n.gsub(/"/, "").chomp.gsub(/ /, "_")}
  f.each_line {|line|
    values = line.split(";").map{|n| n.to_f}
    datum = Hash[*names.zip(values).flatten]
    quality = datum['quality']
    datum.delete('quality')
    cli.train [[quality, Jubatus::Common::Datum.new(datum)]]
  }
}
