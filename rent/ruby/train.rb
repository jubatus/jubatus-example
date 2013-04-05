# -*- coding: utf-8 -*-
require 'jubatus/regression/client'
require 'jubatus/regression/types'
require 'yaml'
require 'pp'

NAME = "A"
filename = ARGV[0].to_s
puts "train by #{filename}"

File.open(filename, "r") {|f|
  f.each_line {|line|
    next if line =~ /^#/
    matched = /^([^,]+),([^,]+),([^,]+),([^,]+),([^,]+),(.*)$/.match(line).captures
    rent, distance, space, age, stair, aspect = *matched
    cli = Jubatus::Regression::Client::Regression.new "127.0.0.1", 9199
    datum = Jubatus::Regression::Datum.new [
                                             ["aspect",aspect],
                                           ],
                                           [
                                             ["space", space.to_f],
                                             ["distance", distance.to_f],
                                             ["age", age.to_f],
                                             ["stair", stair.to_f]
                                           ]
    cli.train NAME, [[rent.to_f, datum]]
    puts "train: 面積#{space.to_f}m^2\t築#{age.to_f}年\t#{stair.to_f}階\t#{aspect}向き -> #{rent}万円"
  }
}
