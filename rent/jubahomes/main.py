import argparse
import yaml

from jubatus.regression.client import regression
from jubatus.regression.types import *
from jubahomes.version import get_version

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

  client = regression('localhost', 9199)
  method = "PA"
  converter = """
    {
      \"string_filter_types\" : {},
      \"string_filter_rules\" : [],
      \"num_filter_types\" : {},
      \"num_filter_rules\" : [],
      \"string_types\" : {},
      \"string_rules\" : [
        {
          \"key\" : \"aspect\",
          \"type\" : \"str\",
          \"sample_weight\" : \"bin\",
          \"global_weight\" : \"bin\"
        }
      ],
      \"num_types\" : {},
      \"num_rules\" : [
        {
          \"key\" : \"*\",
          \"type\" : \"num\"
        }
      ]
    }
  """
  config = config_data(method, converter)

  # train
  num = 0
  if args.traindata:
    client.set_config('', config)
    with open(args.traindata, 'r') as traindata:
      for data in traindata:

        # skip comments
        if not len(data) or data.startswith('#'):
          continue
        num += 1

        rent, distance, space, age, stair, aspect = map(str.strip, data.strip().split(','))
        string_values = [
          ['aspect', aspect]
        ]
        num_values = [
          ['distance', float(distance)],
          ['space', float(space)],
          ['age', float(age)],
          ['stair', float(stair)]
        ]
        d = datum(string_values, num_values)
        train_data = [[float(rent), d]]

        # train
        client.train('', train_data)

    # print train number
    print 'train ...', num

  # anaylze
  with open(args.analyzedata, 'r') as analyzedata:
    myhome = yaml.load(analyzedata)
    string_values = [
      ['aspect', str(myhome['aspect'])]
    ]
    num_values = [
      ['distance', float(myhome['distance'])],
      ['space', float(myhome['space'])],
      ['age', float(myhome['age'])],
      ['stair', float(myhome['stair'])]
    ]
    d = datum(string_values, num_values)
    analyze_data = [d]
    result = client.estimate('', analyze_data)

    print 'rent ....', round(result[0], 1)

