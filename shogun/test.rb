require 'jubatus/classifier/client'
require 'jubatus/classifier/types'
require 'readline'
require 'pp'

NAME = "a"

stty_save = `stty -g`.chomp
trap("INT") { system "stty", stty_save; exit }

while buf = Readline.readline("> ", true)
  cli = Jubatus::Classifier::Client::Classifier.new "127.0.0.1", 9199
  data = Jubatus::Classifier::Datum.new [["name", buf.chomp]], []
  result = cli.classify NAME, [data]
  if 0 < result[0].length
    family = result[0].sort{|a,b| b[1]<=>a[1]}[0][0]
    puts "#{family} #{buf}"
  else
    puts "no match for #{buf}"
  end
end
