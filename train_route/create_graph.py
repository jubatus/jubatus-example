#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
from xml.dom import minidom, Node

from jubatus.graph import client, types

host = '127.0.0.1'
port = 9199
instance_name = ''

stations = {}

class station_join():
    def __init__(self, station1, station2):
        self.station1 = station1
        self.station2 = station2

def get_station_join(line_cd):
    '''
    Create array of `station_join` that represents which stations are connected.

    In this example, we are connecting stations BY NAME, i.e., two stations
    with the same name are regarded as connected and can be transferred to
    each other.
    '''
    join_list = []
    url = 'http://www.ekidata.jp/api/n/' + str(line_cd) + '.xml'
    dom = minidom.parse(urllib.urlopen(url))
    for join_node in dom.getElementsByTagName('station_join'):
        for join_node_child in join_node.childNodes:
            if join_node_child.nodeType == Node.TEXT_NODE:
                continue
            name = join_node_child.nodeName
            value = join_node_child.childNodes.item(0).nodeValue
            if name == 'station_name1':
                station_name1 = value
            elif name == 'station_name2':
                station_name2 = value
        join_list += [ station_join(station_name1, station_name2) ]
    return join_list

def create_graph(c, join_list):
    for join in join_list:
        # Create nodes for stations.
        s1_node_id = add_station(c, join.station1)
        s2_node_id = add_station(c, join.station2)

        # Create bi-directional edge between two nodes.
        edge_info_1 = types.edge_info({}, s1_node_id, s2_node_id)
        edge_info_2 = types.edge_info({}, s2_node_id, s1_node_id)
        c.create_edge(instance_name, s1_node_id, edge_info_1)
        c.create_edge(instance_name, s2_node_id, edge_info_2)

    # Comment-out this line if you're running in distributed mode.
    c.update_index(instance_name)

def add_station(c, name):
    if name in stations:
        node_id = stations[name]
    else:
        node_id = c.create_node(instance_name)
        c.update_node(instance_name, node_id, {'name': name})
        stations[name] = node_id
    return node_id

def print_stations():
    for station in sorted(stations.keys(), key=lambda k: int(stations[k])):
        print "%s\t%s" % (stations[station], station)

if __name__ == '__main__':
    # Create jubagraph client.
    c = client.graph(host, port)

    # Prepare query.
    pq = types.preset_query([], [])
    c.add_shortest_path_query(instance_name, pq)

    # Register stations in each line.
    # Do not add too much lines to prevent causing heavy load to the API server.
    create_graph(c, get_station_join(11302)) # 山手線
    create_graph(c, get_station_join(11312)) # 中央線

    # Print station IDs; you need the ID to search route.
    print "=== Station IDs ==="
    print_stations()
