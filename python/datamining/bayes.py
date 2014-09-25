from __future__ import division
import fileinput


def print_data(data):
    format_cell = lambda c: '{: <16}'.format(c)
    format_row = lambda r: '\t'.join(map(format_cell, r))
    print '\n'.join(map(format_row, data))


if __name__ == '__main__':
    lines = fileinput.input()
    attributes = lines.next().strip().split(',')
    print "Attributes are: " + ', '.join(attributes)
    data = [line.strip().split(',') for line in lines]
    print_data(data)

    e = ['pre-presbyopic', 'hypermetrope', 'yes', 'reduced']

    probs = []

    for c in ['none', 'soft', 'hard']:
        print "--"
        print "Calculating probability for class = " + c
        C = [row for row in data if row[-1] == c]
        P = 1
        l = []
        for i, v in enumerate(e):
            p = len([row for row in C if row[i] == v])
            # d = len([row for row in data if row[i] == v])
            d = len(C)
            dd = len(set([row[i] for row in data]))
            l.append("({0}+1)/({1}+{2})".format(p, d, dd))
            P *= (p + 1) / (d + dd)
            print "C(" + v + "|" + c + ") = " + str(p)

        p = len(C)
        d = len(data)
        dd = len(set([row[-1] for row in data]))
        l.append("({0}+1)/({1}+{2})".format(p, d, dd))
        P *= (p + 1) / (d + dd)
        print "*".join(l)
        print "P(" + c +"|" + ', '.join(e) +") = " + str(P) + " * alpha"
        probs.append(P)


    alpha = 1.0 / sum(probs)
    print "alpha = " + str(alpha)
    for i, c in enumerate(['none', 'soft', 'hard']):
        print "P(" + c +"|" + ', '.join(e) +") = " + str(probs[i] * alpha)

