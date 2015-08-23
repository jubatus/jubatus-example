#!/usr/bin/env python

import sys, json, subprocess
import glob
import random
from jubatus.classifier import client
from jubatus.common import Datum

NAME = "a"
classifier = client.Classifier("127.0.0.1", 9199, NAME)

file_list = glob.glob('../dat/*_train.txt')

fds = [[x.replace("_train.txt", ""), open(x, "r")] for x in file_list]
while fds != []:
    [label, fd] = random.choice(fds)
    text = fd.readline()
    if text == "":
        fds.remove([label, fd])
        print("finished train of label {0} \n".format(label))
        continue
    text_strip = text.rstrip()
    datum = Datum({"text": text_strip})
    print("train {0} : {1} ...".format(label, text_strip))
    classifier.train([(label, datum)])
