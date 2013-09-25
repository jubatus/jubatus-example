#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import httplib

from tweepy.streaming import StreamListener, Stream
from tweepy.auth import OAuthHandler

from jubatus.classifier import client
from jubatus.classifier import types

host = "127.0.0.1"
port = 9199
instance_name = ""

def oauth():
    # Fill in your keys here:
    consumer_key = 'XXXXXXXXXXXXXXXXXXXX'
    consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    access_key = 'XXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    access_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    return auth

def print_color(color, msg, end):
    sys.stdout.write('\033[' + str(color) + 'm' + msg + '\033[0m' + end)

def print_red(msg, end="\n"):
    print_color(31, msg, end)

def print_green(msg, end="\n"):
    print_color(32, msg, end)

class TweetAnalyzer(StreamListener):
    classifier = client.Classifier(host, port, instance_name)

    def __init__(self, highlight):
        super(TweetAnalyzer, self).__init__()
        self.highlight = highlight

    def on_status(self, status):
        if not hasattr(status, 'text'):
            return

        d = types.Datum({'text': status.text});
        result = self.classifier.classify([d])

        if len(result) > 0 and len(result[0]) > 0:
            # sort the result in order of score
            est = sorted(result[0], key=lambda est: est.score, reverse=True)

            print_green(est[0].label, end=" ")
            if est[0].label == self.highlight:
                print_red(status.text)
            else:
                print(status.text)

    def on_error(self, status_code):
        if status_code in httplib.responses:
            status_msg = httplib.responses[status_code]
        else:
            status_msg = str(status_code)
        print "ERROR: Twitter Streaming API returned %d (%s)" % (status_code, status_msg)

        # return False to stop on first error (do not retry)
        return False

def classify_tweets(label):
    stream = Stream(oauth(), TweetAnalyzer(label), secure=True)
    stream.sample()

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            classify_tweets(sys.argv[1])
        else:
            classify_tweets("ja")
    except KeyboardInterrupt:
        print "Stopped."
