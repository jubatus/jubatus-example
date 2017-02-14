#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jubatus
import sys
import csv

def make_table(filename):
    table = []
    with open(filename) as f:
        rows = csv.reader(f, delimiter=',', quotechar='"')
        header = next(rows)
        for row in rows:
            title, authors, groups, keywords, topics, abstract = row
            table.append({"title": title,
                          "authors": authors,
                          "groups": groups,
                          "keywords": keywords,
                          "topics": topics,
                          "abstract": abstract})
    return table

def print_result(query, result, table):
    print("query is : {}".format(table[int(query)]["title"]))
    for r in result:
        print('similar paper is ID:{} "{}"(score: {})'.format(r.id, table[int(r.id)]["title"], r.score))

def main():
    cl = jubatus.NearestNeighbor("localhost", 9199, "nn")
    table = make_table("../data/papers.csv")
    query = sys.argv[1]
    result = cl.similar_row_from_id(query, 4)
    print_result(query, result[1:], table)

if __name__ == "__main__":
    main()

