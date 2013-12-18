#!/usr/bin/env python

import argparse
import yaml

from jubatus.common import Datum
from jubatus.regression.client import Regression
from jubatus.regression.types import *

VERSION = (0, 0, 1, '')

def get_version():
  version_string = '%s.%s.%s' % VERSION[0:3]
  if len(VERSION[3]):
    version_string += '-' + VERSION[3]
  return version_string

def parse_options():
  parser = argparse.ArgumentParser()
  parser.add_argument(
    '-a',
    required = True,
    help     = 'analyze data file (YAML)',
    metavar  = 'FILE',
    dest     = 'analyzedata'
  )
  parser.add_argument(
    '-t',
    help     = 'train data file (CSV)',
    metavar  = 'FILE',
    dest     = 'traindata'
  )
  parser.add_argument(
    '-v',
    '--version',
    action   = 'version',
    version  = '%(prog)s ' + get_version()
  )
  return parser.parse_args()

def main():
  args = parse_options()

  client = Regression('127.0.0.1', 9199, '')

  # train
  num = 0
  if args.traindata:
    with open(args.traindata, 'r') as traindata:
      for data in traindata:

        # skip comments
        if not len(data) or data.startswith('#'):
          continue
        num += 1

        rent, distance, space, age, stair, aspect = map(str.strip, data.strip().split(','))
        d = Datum({
            'aspect': aspect,
            'distance': float(distance),
            'space': float(space),
            'age': float(age),
            'stair': float(stair) })
        train_data = [[float(rent), d]]

        # train
        client.train(train_data)

    # print train number
    print 'train ...', num

  # anaylze
  with open(args.analyzedata, 'r') as analyzedata:
    myhome = yaml.load(analyzedata)
    d = Datum({
        'aspect': str(myhome['aspect']),
        'distance': float(myhome['distance']),
        'space': float(myhome['space']),
        'age': float(myhome['age']),
        'stair': float(myhome['stair'])
        })
    analyze_data = [d]
    result = client.estimate(analyze_data)

    print 'rent ....', round(result[0], 1)

if __name__ == '__main__':
    main()

