#!/usr/bin/env ruby
# -*- coding: utf-8 -*-

$host = "127.0.0.1"
$port = 9199

$name = "recommender_baseball"

require 'rubygems'
require 'jubatus/recommender/client'
require 'jubatus/recommender/types'

recommender =
	Jubatus::Recommender::Client::Recommender.new($host,$port)
open("dat/baseball.csv") {|f|
	f.each{|line|
		pname, team, bave, games, pa, atbat, hit, homerun, runsbat,
			stolen, bob, hbp, strikeout, sacrifice, dp, slg, obp,
			ops, rc27, xr27 = line.split(",")
		sr = recommender.similar_row_from_id($name, pname, 4)
		puts("player #{pname} is similar to : #{sr[1][0]} #{sr[2][0]} #{sr[3][0]}")
	}
}
