require 'jubatus/classifier/client'
require 'readline'
require 'pp'

NAME = "a"

stty_save = `stty -g`.chomp
trap("INT") { system "stty", stty_save; exit }

while buf = Readline.readline("> ", true)
  cli = Jubatus::Classifier::Client::Classifier.new "127.0.0.1", 9199, NAME
  data = Jubatus::Common::Datum.new("name" => buf.chomp)
  result = cli.classify [data]
  if 0 < result[0].length
    family = result[0].max_by{|x| x.score}.label
    puts "#{family} #{buf}"
  else
    puts "no match for #{buf}"
  end
end
