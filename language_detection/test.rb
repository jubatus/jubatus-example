require 'jubatus/classifier/client'
require 'readline'
require 'pp'

NAME = "a"

stty_save = `stty -g`.chomp
trap("INT") { system "stty", stty_save; exit }

while buf = Readline.readline("> ", true)
  #next if buf == ''
  if buf == "" then
    break
  end
  cli = Jubatus::Classifier::Client::Classifier.new "127.0.0.1", 9199, NAME
  data = Jubatus::Common::Datum.new("text" => buf.chomp)
  result = cli.classify [data]
  pp result[0].sort_by{|x| -x.score}
end
