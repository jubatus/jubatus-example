#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from jubatus.graph import client, types

host = '127.0.0.1'
port = 9199
instance_name = ''

def search_route(from_id, to_id):
    c = client.graph(host, port)

    pq = types.preset_query([], [])
    spreq = types.shortest_path_req(from_id, to_id, 100, pq)
    stations = c.shortest_path(instance_name, spreq)

    print "Pseudo-Shortest Path (hops) from %s to %s:" % (from_id, to_id)
    for station in stations:
        node = c.get_node(instance_name, station)
        station_name = ''
        if 'name' in node.p:
            station_name = node.p['name']
        print "  %s\t%s" % (station, station_name)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: %s from_station_id to_station_id" % sys.argv[0]
        sys.exit(1)
    search_route(str(sys.argv[1]), str(sys.argv[2]))
