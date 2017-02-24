#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jubatus
from jubatus.common import Datum
import csv
import argparse

def make_datum(row, args):
    title, authors, groups, keywords, topics, abstract = row
    d = Datum()
    d.add_string("title", title)
    if args.abstract:
        d.add_string("abstract", abstract)
    return d
    
def set_rows(filename, args):
    with open(filename) as f:
        rows = csv.reader(f, delimiter=',', quotechar='"')
        header = next(rows)
        cl = jubatus.NearestNeighbor("localhost", 9199, "nn")
        cl.clear()
        for i, r in enumerate(rows):
            d = make_datum(r, args)
            cl.set_row(str(i), d)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--abstract", action="store_true", default="false")
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    set_rows("../data/papers.csv", args)

if __name__ == "__main__":
    main()
