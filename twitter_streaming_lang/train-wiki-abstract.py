#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import xml.sax, xml.sax.handler

from jubatus.classifier import client
from jubatus.classifier import types

host = "127.0.0.1"
port = 9199
instance_name = ""

class Handler(xml.sax.handler.ContentHandler):
    read = False
    count = 0

    def __init__(self, classifier, label):
        self.classifier = classifier
        self.label = label

    def startElement(self, name, attrs):
        if name == "abstract":
            self.read = True

    def endElement(self, name):
        self.read = False

    def characters(self, content):
        if not self.read:
            return

        d = types.datum([], [])
        d.string_values = [
            ['text', content],
        ]
        self.classifier.train(instance_name, [[self.label, d]])
        self.count += 1
        if (self.count % 1000 == 0):
            print "Training(%s): %d ..." % (self.label, self.count)

def train_wikipedia_abstract(label, xmlfile):
    classifier = client.classifier(host, port)
    algorithm = "AROW"
    config = {
        "num_filter_types": {
        },
        "num_filter_rules": [
        ],
        "string_filter_types": {
        },
        "string_filter_rules": [
        ],
        "num_types": {
        },
        "num_rules": [
        ],
        "string_types": {
            "bigram":  { "method": "ngram", "char_num": "2" }
        },
        "string_rules": [
            { "key": "*", "type": "bigram", "sample_weight": "bin", "global_weight": "bin" }
        ]
    }

    classifier.set_config(instance_name, types.config_data(algorithm, json.dumps(config)))

    parser = xml.sax.make_parser()
    parser.setContentHandler(Handler(classifier, label))
    parser.parse(xmlfile)

if __name__ == '__main__':
    try:
        if len(sys.argv) != 3:
            print "Usage: %s LANG LANGwiki-latest-abstract.xml" % sys.argv[0]
            sys.exit(1)
        else:
            label = sys.argv[1]
            xmlfile = sys.argv[2]
            train_wikipedia_abstract(label, xmlfile)
    except KeyboardInterrupt:
        print "Stopped."
