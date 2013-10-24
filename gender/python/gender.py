#!/usr/bin/env python

host = '127.0.0.1'
port = 9199
name = 'test'

import jubatus
from jubatus.common import Datum

client = jubatus.Classifier(host, port, name)

train_data = [
    ('male',   Datum({'hair': 'short', 'top': 'sweater', 'bottom': 'jeans', 'height': 1.70})),
    ('female', Datum({'hair': 'long',  'top': 'shirt',   'bottom': 'skirt', 'height': 1.56})),
    ('male',   Datum({'hair': 'short', 'top': 'jacket',  'bottom': 'chino', 'height': 1.65})),
    ('female', Datum({'hair': 'short', 'top': 'T shirt', 'bottom': 'jeans', 'height': 1.72})),
    ('male',   Datum({'hair': 'long',  'top': 'T shirt', 'bottom': 'jeans', 'height': 1.82})),
    ('female', Datum({'hair': 'long',  'top': 'jacket',  'bottom': 'skirt', 'height': 1.43})),
#    ('male',   Datum({'hair': 'short', 'top': 'jacket',  'bottom': 'jeans', 'height': 1.76})),
#    ('female', Datum({'hair': 'long',  'top': 'sweater', 'bottom': 'skirt', 'height': 1.52})),
    ]

client.train(train_data)

test_data = [
    Datum({'hair': 'short', 'top': 'T shirt', 'bottom': 'jeans', 'height': 1.81}),
    Datum({'hair': 'long',  'top': 'shirt',   'bottom': 'skirt', 'height': 1.50}),
]

results = client.classify(test_data)

for result in results:
    for r in result:
        print(r.label, r.score)
    print
