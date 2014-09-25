from sys import argv
import fileinput


if __name__ == '__main__':
    lines = fileinput.input(argv[1])
    classifier = __import__(argv[2])
    lines.next()  # Skip the first line, which are the column names
    for line in lines:
        cols = line.strip().split("\t")
        print '\t'.join(cols) + ' - ' + classifier.classify(*cols)


