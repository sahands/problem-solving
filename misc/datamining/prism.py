from __future__ import division
import fileinput


def print_data(data):
    print '\n'.join('\t'.join('{: <16}'.format(s) for s in row)
                    for row in data)


def build_rule(data, attributes, used_attributes, target_class):
    # print_data(data)
    print "--"
    best_accuracy = (-1, 1)
    best_rule = None
    best_covered = []
    # print "Target class value = " + target_class
    for i in xrange(len(attributes) - 1):
        if i in used_attributes:
            continue
        a_values = set(row[i] for row in data)
        for v in a_values:
            covered = list(row for row in data if row[i] == v)
            uncovered = list(row for row in data if row[i] != v)
            positive = list(row for row in covered if row[-1] == target_class)
            print "{0: <15}\t ==\t {1: <8} \t {2}/{3}".format(attributes[i],
                                                              v,
                                                              len(positive),
                                                              len(covered))
            left = len(positive) * best_accuracy[1]
            right = len(covered) * best_accuracy[0]
            # print best_accuracy, len(positive), len(covered), left, right
            if (left == right and len(covered) > best_accuracy[1]) or left > right:
                best_accuracy = (len(positive), len(covered))
                best_rule = (i, v)
                best_uncovered = uncovered
                best_covered = covered

    if best_rule is None:
        return (0.0, 1.0), "", []
    rule = "{0} == {1}".format(attributes[best_rule[0]], best_rule[1])

    if best_accuracy[0] < best_accuracy[1] and \
            len(used_attributes) < len(attributes) - 1:
        used_attributes.append(best_rule[0])
        aux_acc, aux_rule, aux_uncovered = build_rule(best_covered,
                                                      attributes,
                                                      used_attributes,
                                                      target_class)
        used_attributes.pop()
        rule += " and " + aux_rule
        best_uncovered += aux_uncovered
        best_accuracy = aux_acc

    print rule
    print "Accuracy = {0}/{1}".format(best_accuracy[0], best_accuracy[1])
    print "---"
    return best_accuracy, rule, best_uncovered


def test_rule(data, attributes, target_class):
    ac, rule1, uncovered = build_rule(data, attributes, [], target_class)
    print '====='
    print rule1
    print '====='
    return uncovered

if __name__ == '__main__':
    lines = fileinput.input()
    attributes = lines.next().strip().split(',')
    print "Attributes are: " + ', '.join(attributes)
    data = [line.strip().split(',') for line in lines]
    target_class = 'yes'
    uncovered = test_rule(data, attributes, target_class)
    uncovered = test_rule(uncovered, attributes, target_class)
