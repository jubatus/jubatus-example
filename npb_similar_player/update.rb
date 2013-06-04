#!/usr/bin/env ruby 
# -*- coding: utf-8 -*-

$host = "127.0.0.1"
$port = 9199
$name = "test"

require 'rubygems'
require 'json'

require 'jubatus/recommender/client'
require 'jubatus/recommender/types'

$name = "recommender_baseball";

def update(recommender)
	open("dat/baseball.csv") {|f|
		f.each {|line|
			pname, team, bave, games, pa, atbat, hit, homerun, runsbat, stolen, bob, hbp, strikeout, sacrifice, dp, slg, obp, ops, rc27, xr27 = line.split(",")

			datum = Jubatus::Recommender::Datum.new(
				[
					["チーム",team]
			],
				[
					["打率", bave.to_f],
					["試合数", games.to_f],
					["打席", pa.to_f],
					["打数", atbat.to_f],
					["安打", hit.to_f],
					["本塁打", homerun.to_f],
					["打点", runsbat.to_f],
					["盗塁", stolen.to_f],
					["四球", bob.to_f],
					["死球", hbp.to_f],
					["三振", strikeout.to_f],
					["犠打", sacrifice.to_f],
					["併殺打", dp.to_f],
					["長打率", slg.to_f],
					["出塁率", obp.to_f],
					["OPS", ops.to_f],
					["RC27", rc27.to_f],
					["XR27", xr27.to_f]
			]
			)
			recommender.update_row($name, pname, datum)
		}
	}
end

recommender = Jubatus::Recommender::Client::Recommender.new($host, $port)
update(recommender)
