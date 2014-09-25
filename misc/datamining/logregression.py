from __future__ import division
import fileinput
import math


__author__ = "Sahand Saba"
__email__ = "saba@uvic.ca"


EPS = 0.000001


def dot(u, v):
    """
    Returns the dot product of vectors u and v. Assumes len(v) = len(u).
    """
    return sum(x * y for x, y in zip(u, v))


def prob(x, w):
    return 1.0 / (1 + math.exp(-dot(w, x)))


def print_data(data, attributes, w):
    attributes = attributes + ['Est. + Prob.']
    format_col = lambda c: '{: <8}'.format(c)
    format_row = lambda r: '\t'.join(format_col(s) for s in r + [prob(r, w)])
    print '\t'.join('{: <8}'.format(s) for s in attributes)
    print '\n'.join(format_row(row) for row in data)
    print ""


def log_regression(data, attributes, class_index, kappa):
    """
    Returns a generator for the weights w of a logarithmic regression
    best estimating the data set. Assumes the data set is normalized already.
    """
    # k is the number of attributes minus the class attribute
    k = len(attributes) - 1
    # n is the number of training data instances
    n = len(data)
    # w is the weight vector, which we initialize to k zeros (not k + 1 since
    # data is normalized and already has a column for the "dummy" variable.)
    w = [0] * k
    # Each iteration of this infinite loop yields the next iteration
    # of weights.
    while(True):
        yield w
        # First calculate the gradient vector
        g = [0] * k

        w_dot_x = [dot(w, x) for x in data]
        for j in xrange(k):
            for i, x in enumerate(data):
                y_i = x[class_index]
                g[j] += (x[j] * y_i) / (1 + math.exp(y_i * w_dot_x[i]))
            g[j] /= n

        # if the gradient's length is very small then end the iteration since
        # further iterations will not improve the accuracy by much
        if dot(g, g) < EPS:
            return

        # Addition above instead of subtration, and addition here again
        # instead of - kappa * g[i]. They cancel each other out :)
        w = [w[i] + kappa * g[i] for i in xrange(k)]


if __name__ == '__main__':
    kappa = 2.0
    lines = fileinput.input()
    attributes = lines.next().strip().split()
    print "Attributes are: " + ', '.join(attributes)
    data = [[float(x) for x in line.strip().split()] for line in lines]
    # -1 indicates that the class attribute is the last attribute
    regression = log_regression(data, attributes, -1, kappa)
    for i, w in enumerate(regression):
        print "Iteration {0}: w = {1}".format(i, str(w))
        print_data(data, attributes, w)
        if i == 51:
            break
