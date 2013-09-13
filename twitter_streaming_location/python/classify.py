#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from jubatus.classifier import client
from jubatus.classifier import types

# Jubatus configuration
host = "127.0.0.1"
port = 9199
instance_name = "" # required only when using distributed mode

def estimate_location_for(text):
    classifier = client.classifier(host, port)

    # Create datum for Jubatus
    d = types.Datum([], [])
    d.string_values = [('text', text)]

    # Send estimation query to Jubatus
    result = classifier.classify(instance_name, [d])

    if len(result[0]) > 0:
        # Sort results by score
        est = sorted(result[0], key=lambda e: e.score, reverse=True)

        # Print the result
        print "Estimated Location for %s:" % text
        for e in est:
            print "  " + e.label + " (" + str(e.score) + ")"
    else:
        # No estimation results; maybe we haven't trained enough
        print "No estimation results available."
        print "Train more tweets or try using another text."

if __name__ == '__main__':
    if len(sys.argv) == 2:
        estimate_location_for(sys.argv[1])
    else:
        print "Usage: %s tweet_text" % sys.argv[0]
