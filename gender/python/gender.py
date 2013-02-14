#!/usr/bin/env python

host = '127.0.0.1'
port = 9199
name = 'test'

import jubatus
from jubatus.classifier.types import datum

client = jubatus.Classifier(host, port)

train_data = [
    ('male',   datum([('hair', 'short'), ('top', 'sweater'), ('bottom', 'jeans')], [('height', 1.70)])),
    ('female', datum([('hair', 'long'),  ('top', 'shirt'),   ('bottom', 'skirt')], [('height', 1.56)])),
    ('male',   datum([('hair', 'short'), ('top', 'jacket'),  ('bottom', 'chino')], [('height', 1.65)])),
    ('female', datum([('hair', 'short'), ('top', 'T shirt'), ('bottom', 'jeans')], [('height', 1.72)])),
    ('male',   datum([('hair', 'long'),  ('top', 'T shirt'), ('bottom', 'jeans')], [('height', 1.82)])),
    ('female', datum([('hair', 'long'),  ('top', 'jacket'),  ('bottom', 'skirt')], [('height', 1.43)])),
#    ('male',   datum([('hair', 'short'), ('top', 'jacket'),  ('bottom', 'jeans')], [('height', 1.76)])),
#    ('female', datum([('hair', 'long'),  ('top', 'sweater'), ('bottom', 'skirt')], [('height', 1.52)])),
    ]

client.train(name, train_data)

test_data = [
    datum([('hair', 'short'), ('top', 'T shirt'), ('bottom', 'jeans')], [('height', 1.81)]),
    datum([('hair', 'long'),  ('top', 'shirt'),   ('bottom', 'skirt')], [('height', 1.50)]),
]

results = client.classify(name, test_data)

for result in results:
    for r in result:
        print r.label, r.score
    print
