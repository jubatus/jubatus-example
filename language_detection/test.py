#!/usr/bin/env python

import json, commands
from jubatus.classifier import client
from jubatus.classifier import types

while True:
    buf = raw_input("> ")
    if buf == "":
        break
    classifier = client.Classifier("127.0.0.1", 9199, "")
    datum = types.Datum({"text": buf.rstrip()})
    result = classifier.classify([datum])
    if len(result[0]) == 0:
        print("nothing")
        continue
    result[0].sort(key = lambda x:x.score, reverse = True)
    for res in result[0]:
        print(res.label + " -> " + str(res.score))
