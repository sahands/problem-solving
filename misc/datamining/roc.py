from __future__ import division
import fileinput
import math


__author__ = "Sahand Saba"
__email__ = "saba@uvic.ca"


def print_data(data):
    print '\n'.join('\t'.join('{: <16}'.format(s) for s in row) for row in data)
    print ""


def roc(data, class_index, classifier_index):
    r = {}
    data.sort(key=lambda row: float(row[classifier_index]))
    print_data(data)
    P = sum(1 for row in data if row[class_index] == '+')
    N = len(data) - P
    FP = N
    TP = P
    # At threshold zero every positive is a true positive
    # And every negative is a false positive, since everything
    # will be classified as postivie.
    r[0] = (FP / N, TP / P)
    for row in data:
        if row[class_index] == '+':
            TP -= 1
        else:
            FP -= 1
        r[float(row[classifier_index])] = (FP / N, TP / P)

    return r


if __name__ == '__main__':
    lines = fileinput.input()
    # attributes = lines.next().strip().split()
    # print "Attributes are: " + ', '.join(attributes)
    data = [[x.strip() for x in line.split(',')] for line in lines]
    print_data(data)
    roc1 = roc(data, 1, 2)
    print roc1.items()
    print '\n'.join('({0}, {1}) [{2}]'.format(x, y, k)
            for (x, y), k in sorted(zip(roc1.values(), roc1.keys())))
    roc2 = roc(data, 1, 3)
    print '\n'.join('({0}, {1}) [{2}]'.format(x, y, k)
            for (x, y), k in sorted(zip(roc2.values(), roc1.keys())))
    print roc2.items()

