require 'jubatus/classifier/client'
require 'pp'

NAME = "a"
cli = Jubatus::Classifier::Client::Classifier.new "127.0.0.1", 9199, NAME

file_list = Dir.glob("../dat/*_train.txt")
pp file_list
begin
  fds = file_list.map {|m|
    [ m.gsub(/_train\.txt/, ""),
      File.open(m, "r")
    ]
  }
  while !fds.empty?
    label, fd = *fds.sample
    text = fd.gets
    if text.nil?
      fds.delete_if {|a| a[0] == label}
      puts "finished train of  label:#{label}"
      next
    end
    next if text == ""
    text.chomp!
    datum = Jubatus::Common::Datum.new("text" => text)
    puts "train #{label} : #{text.slice(0,60)} ..."
    cli.train([[label, datum]])
  end
rescue => e
  pp e
ensure
  fds.each{|fd|
    begin
      fd[1].close
    rescue => e
    end
  }
end

cli.save "inner"
