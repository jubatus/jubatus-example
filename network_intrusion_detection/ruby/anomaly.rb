#!/usr/bin/env ruby
# -*- coding: utf-8 -*-

$host = "127.0.0.1"
$port = 9199
$name = "test"

require 'json'

require 'jubatus/anomaly/client'

# 0. set keyboard interruption handler"
Signal.trap(:INT) {
    print "You pressed Ctrl+C."
    print "Stop running the job."
    exit(0)
}

# 1. Configuration to connect Jubatus Server
client = Jubatus::Anomaly::Client::Anomaly.new($host, $port, $name)

# 2. prepare training dataset
open("../kddcup.data_10_percent.txt") { |f|
	f.each { |line|
		duration, protocol_type, service, flag, src_bytes, dst_bytes, land, wrong_fragment, urgent, hot, num_failed_logins, logged_in, num_compromised, root_shell, su_attempted, num_root, num_file_creations, num_shells, num_access_files, num_outbound_cmds, is_host_login, is_guest_login, count, srv_count, serror_rate, srv_serror_rate, rerror_rate, srv_rerror_rate, same_srv_rate, diff_srv_rate, srv_diff_host_rate, dst_host_count, dst_host_srv_count, dst_host_same_srv_rate, dst_host_diff_srv_rate, dst_host_same_src_port_rate, dst_host_srv_diff_host_rate, dst_host_serror_rate, dst_host_srv_serror_rate, dst_host_rerror_rate, dst_host_srv_rerror_rate, label = line.split(",")
                data = Jubatus::Common::Datum.new(
				"protocol_type" => protocol_type,
				"service" => service,
				"flag" => flag,
				"land" => land,
				"logged_in" => logged_in,
				"is_host_login" => is_host_login,
				"is_guest_login" => is_guest_login,
		    		"duration" => duration.to_f,
				"src_bytes" => src_bytes.to_f,
				"dst_bytes" => dst_bytes.to_f,
				"wrong_fragment" => wrong_fragment.to_f,
				"urgent" => urgent.to_f,
				"hot" => hot.to_f,
				"num_failed_logins" => num_failed_logins.to_f,
				"num_compromised" => num_compromised.to_f,
				"root_shell" => root_shell.to_f,
				"su_attempted" => su_attempted.to_f,
				"num_root" => num_root.to_f,
				"num_file_creations" => num_file_creations.to_f,
				"num_shells" => num_shells.to_f,
				"num_access_files" => num_access_files.to_f,
				"num_outbound_cmds" => num_outbound_cmds.to_f,
				"count" => count.to_f,
				"srv_count" => srv_count.to_f,
				"serror_rate" => serror_rate.to_f,
				"srv_serror_rate" => srv_serror_rate.to_f,
				"rerror_rate" => rerror_rate.to_f,
				"srv_rerror_rate" => srv_rerror_rate.to_f,
				"same_srv_rate" => same_srv_rate.to_f,
				"diff_srv_rate" => diff_srv_rate.to_f,
				"srv_diff_host_rate" => srv_diff_host_rate.to_f,
				"dst_host_count" => dst_host_count.to_f,
				"dst_host_srv_count" => dst_host_srv_count.to_f,
				"dst_host_same_srv_rate" => dst_host_same_srv_rate.to_f,
				"dst_host_same_src_port_rate" => dst_host_same_src_port_rate.to_f,
				"dst_host_diff_srv_rate" => dst_host_diff_srv_rate.to_f,
				"dst_host_srv_diff_host_rate" => dst_host_srv_diff_host_rate.to_f,
				"dst_host_serror_rate" => dst_host_serror_rate.to_f,
				"dst_host_srv_serror_rate" => dst_host_srv_serror_rate.to_f,
				"dst_host_rerror_rate" => dst_host_rerror_rate.to_f,
				"dst_host_srv_rerror_rate" => dst_host_srv_rerror_rate.to_f)
		# 3. training
                ret = client.add(data)


		# 4. output results
                if (ret.score != Float::INFINITY) and (ret.score != 1.0) then
                    print ret, ' ', label
                end
        }
}
