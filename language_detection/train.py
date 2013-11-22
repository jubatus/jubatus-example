#!/usr/bin/env python

import sys, json, subprocess
import random
from jubatus.classifier import client
from jubatus.classifier import types

NAME = "a"
classifier = client.Classifier("127.0.0.1", 9199, NAME)

file_list = subprocess.Popen(["ls | grep _train.txt"],
                             stdout = subprocess.PIPE,
                             shell = True).communicate()[0].split('\n')[0:-1]

fds = map(lambda x: [x.replace("_train.txt", ""), open(x, "r")], file_list)
while fds != []:
    [label, fd] = random.choice(fds)
    text = fd.readline()
    if text == "":
        fds.remove([label, fd])
        print("finished train of label %s \n" % (label))
        continue
    text_strip = text.rstrip()
    datum = types.Datum({"text": text_strip})
    print("train %s : %s ..." %(label, text_strip))
    classifier.train([(label, datum)])
