require 'jubatus/classifier/client'
require 'jubatus/classifier/types'
require 'readline'
require 'pp'

NAME = "a"

stty_save = `stty -g`.chomp
trap("INT") { system "stty", stty_save; exit }

while buf = Readline.readline("> ", true)
  #next if buf == ''
  cli = Jubatus::Classifier::Client::Classifier.new "127.0.0.1", 9199
  data = Jubatus::Classifier::Datum.new [["text", buf.chomp]], []
  result = cli.classify NAME, [data]
  pp result[0].sort{|a,b| b[1]<=>a[1]}
end
