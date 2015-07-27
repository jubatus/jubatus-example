#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import re
import httplib

from tweepy.streaming import StreamListener, Stream
from tweepy.auth import OAuthHandler

from jubatus.classifier import client
from jubatus.common import Datum

def oauth():
    # Fill in your keys here:
    consumer_key = 'XXXXXXXXXXXXXXXXXXXX'
    consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    access_key = 'XXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    access_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    return auth

# Jubatus Configuration
host = "127.0.0.1"
port = 9199
instance_name = "" # required only when using distributed mode

def print_color(color, msg, end):
    sys.stdout.write('\033[' + str(color) + 'm' + str(msg) + '\033[0m' + str(end))

def print_red(msg, end="\n"):
    print_color(31, msg, end)

def print_green(msg, end="\n"):
    print_color(32, msg, end)

class Trainer(StreamListener):
    classifier = client.Classifier(host, port, instance_name)

    def __init__(self, locations):
        super(Trainer, self).__init__()
        self.locations = locations

    '''
    Format of 'status' can be found in:
        https://dev.twitter.com/docs/platform-objects/tweets
    '''
    def on_status(self, status):
        if not hasattr(status, 'text'):
            return
        if not hasattr(status, 'coordinates'):
            return
        if not status.coordinates or not 'coordinates' in status.coordinates:
            return

        loc = None
        for l in self.locations:
            coordinates = status.coordinates['coordinates']
            if l.is_inside(coordinates[0], coordinates[1]):
                loc = l
                break
        if not loc:
            # Unknown location
            return
        hashtags = status.entities['hashtags']
        detagged_text = remove_hashtags_from_tweet(status.text, hashtags)

        # Create datum for Jubatus
        d = Datum({'text': detagged_text})

        # Send training data to Jubatus
        self.classifier.train([(loc.name, d)])

        # Print trained tweet
        print_green(loc.name, ' ')
        print detagged_text

    def on_error(self, status_code):
        if status_code in httplib.responses:
            status_msg = httplib.responses[status_code]
        else:
            status_msg = str(status_code)
        print "ERROR: Twitter Streaming API returned %d (%s)" % (status_code, status_msg)

        # return False to stop on first error (do not retry)
        return False

class LocationFence(object):
    def __init__(self, name, longitude1, latitude1, longitude2, latitude2):
        self.name = name
        self.longitude1 = longitude1
        self.latitude1 = latitude1
        self.longitude2 = longitude2
        self.latitude2 = latitude2

    def is_inside(self, longitude, latitude):
        return \
            self.longitude1 <= longitude and longitude <= self.longitude2 and \
            self.latitude1 <= latitude and latitude <= self.latitude2

    def get_coordinates(self):
        return [self.longitude1, self.latitude1, self.longitude2, self.latitude2]

def remove_hashtags_from_tweet(tweet, hashtags):
    indices = {} # ranges to exclude from the tweet text (begin->end)
    for hashtag in hashtags:
        indices[hashtag['indices'][0]] = hashtag['indices'][1]
    pos = 0
    text = u''
    for begin in sorted(indices.keys()):
        text += tweet[pos:begin]
        pos = indices[begin]
    text += tweet[pos:]
    return text

def train_tweets():
    tokyo    = LocationFence("Tokyo",    138.946381, 35.523285, 139.953232, 35.906849)
    hokkaido = LocationFence("Hokkaido", 139.546509, 41.393294, 145.742798, 45.729191)
    kyusyu   = LocationFence("Kyusyu",   129.538879, 31.147006, 131.856995, 33.934245)

    locations = [tokyo, hokkaido, kyusyu]
    request_coordinates = []
    for l in locations:
        request_coordinates += l.get_coordinates()

    stream = Stream(oauth(), Trainer(locations), secure=True)
    stream.filter(locations=request_coordinates)

if __name__ == '__main__':
    try:
        train_tweets()
    except KeyboardInterrupt:
        print "Stopped."
