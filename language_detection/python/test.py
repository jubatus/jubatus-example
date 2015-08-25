#!/usr/bin/env python

import json
import subprocess
from jubatus.classifier import client
from jubatus.common import Datum

while True:
    try:
        # for Python 2
        input_func = raw_input
    except NameError:
        # for Python 3
        input_func = input
        # pass
    if input_func == "":
        break
    classifier = client.Classifier("127.0.0.1", 9199, "")
    datum = Datum({"text": input_func("> ").rstrip()})
    result = classifier.classify([datum])
    if len(result[0]) == 0:
        print("nothing")
        continue
    result[0].sort(key=lambda x: x.score, reverse=True)
    for res in result[0]:
        print(res.label + " -> " + str(res.score))
