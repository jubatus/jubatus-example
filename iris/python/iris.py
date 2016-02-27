# -*- coding: utf-8 -*-

host = '127.0.0.1'
port = 9199
name = 'iris'

import csv
import random

from jubatus import Classifier
from jubatus.common import Datum
from jubatus.classifier.types import LabeledDatum

def load_iris():
    header = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    dataset = []
    with open('../iris.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            values = row[:4]
            for i in range(len(values)):
                values[i] = float(values[i])
            label = row[4]
            dataset.append((label, Datum(dict(zip(header, values)))))
    return dataset

def split_train_test(dataset, k):
    random.shuffle(dataset)
    train_data = dataset[:len(dataset) / k * (k - 1)]
    test_data = dataset[len(dataset) / k * (k - 1):]
    return train_data, test_data

def train(classifier, train_data):
    for data in train_data:
        classifier.train([LabeledDatum(data[0], data[1])])

def test(classifier, test_data):
    count_ok, count_ng = 0, 0
    for data in test_data:
        predict = classifier.classify([data[1]])
        estimated = get_most_likely(predict[0])
        answer = data[0]
        if estimated == answer:
            print("OK, answer:{0}, estimated:{1}".format(answer, estimated))
            count_ok += 1
        else:
            print("NG, answer:{0}, estimated:{1}".format(answer, estimated))
            pass
    accuracy = float(count_ok) / float(len(test_data))
    print("------------------")
    print("OK: {0}".format(count_ok))
    print("NG: {0}".format(len(test_data) - count_ok))
    print("Accuracy: {0}".format(float(count_ok) / float(len(test_data))))
    return accuracy

def get_most_likely(result):
    max_score = float('-inf')
    max_label = ''
    for r in result:
        if r.score > max_score:
            max_score = r.score
            max_label = r.label
    return max_label
 
def run(k = 4):
    classifier = Classifier(host, port, name)
    dataset = load_iris()
    train_data, test_data  = split_train_test(dataset, k)
    train(classifier, train_data)
    accuracy = test(classifier, test_data)
    return accuracy

if __name__ == '__main__':
    run()
