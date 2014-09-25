from __future__ import division
import fileinput
import math
from itertools import groupby


__author__ = "Sahand Saba"
__email__ = "saba@uvic.ca"


class ID3TreeNode(object):
    attribute = None
    children = dict()

    def __init__(self, attribute):
        self.attribute = attribute
        self.children = dict()

    def add_child(self, attribute_value, child):
        self.children[attribute_value] = child

    def __str__(self, spaces=""):
        result = ""
        for key, value in self.children.items():
            result += spaces + "if " + str(self.attribute) + " == '" + key + "':\n"
            if isinstance(value, basestring):
                result += spaces + "\treturn '" + value + "'\n"
            else:
                result += value.__str__(spaces + "\t")
        return result


def print_data(data):
    print '\n'.join('\t'.join('{: <16}'.format(s) for s in row) for row in data)
    print ""


def entropy(data, attribute_index, class_values, class_index):
    entropy = 0.0
    attribute_getter = lambda row: row[attribute_index]
    data.sort(key=attribute_getter)
    for value, group in groupby(data, attribute_getter):
        group = list(group)
        # print "Attribute value " + value + " has " + str(len(group)) + " items."
        probabilities = [len([row for row in group if row[class_index] == class_value]) / len(group)
                         for class_value in class_values]
        # print "Probability distribution for " + value + ": "
        cur_entropy = len(group) * sum(p * math.log(p) for p in probabilities if p > 0.0001)
        print value + ": Entropy(" + ', '.join('{:1.3f}'.format(p) for p in probabilities) + \
            ") = " + '{:.3f}'.format(-cur_entropy/len(data))
        entropy += cur_entropy
        # print "Entropy for probability distribution = " + '{:.3f}'.format(-cur_entropy)

    return -entropy / len(data)


def build_id3_tree(data, attributes, class_index, used_up_attributes):
    class_values = set(row[-1] for row in data)
    if len(class_values) == 1 or len(used_up_attributes) >= len(attributes) - 1:
        return data[0][class_index]

    print "------- Building tree for data: --------"
    print_data(data)

    best_entropy = float("inf")
    best_attribute = None
    for attribute_index in xrange(len(attributes)):
        if attributes[attribute_index] == attributes[class_index]:
            continue
        if attribute_index in used_up_attributes:
            continue

        print "Calculating entropy for split using attribute: " + attributes[attribute_index]
        e = entropy(data, attribute_index, class_values, class_index)
        print "Entropy for split = " + '{:.3f}'.format(e)
        if e < best_entropy:
            best_entropy = e
            best_attribute = attribute_index

    print "Best split is using " + attributes[best_attribute]
    print "With entropy " + '{:.3f}'.format(best_entropy)

    root = ID3TreeNode(attributes[best_attribute])
    used_up_attributes.append(best_attribute)
    attribute_getter = lambda row: row[best_attribute]
    data.sort(key=attribute_getter)
    for value, group in groupby(data, attribute_getter):
        group = list(group)
        child = build_id3_tree(group, attributes, class_index, used_up_attributes)
        root.add_child(value, child)
    used_up_attributes.pop()

    return root


if __name__ == '__main__':
    lines = fileinput.input()
    attributes = lines.next().strip().split(',')
    print "Attributes are: " + ', '.join(attributes)
    data = [line.strip().split(',') for line in lines]
    id3 = build_id3_tree(data, attributes, -1, [])
    print "Final ID3 tree Python classifier for data:\n"
    print "def classify(" + ', '.join(attributes) + '):'
    print id3.__str__("\t")
