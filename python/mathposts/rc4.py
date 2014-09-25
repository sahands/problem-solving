import random
import unittest


class RC4KeyStream(object):
    key = None
    permutation = None
    i, j = 0, 0

    def __init__(self, key, permutation_length=256):
        # First transform the key from string to list of numbers if necessary
        if isinstance(key, basestring):
            key = [ord(c) for c in key]

        p = self.permutation = range(permutation_length)  # set to the identity permutation
        self.key = key
        self.i = self.j = 0
        j = 0
        for i in xrange(permutation_length):
            j = (j + p[i] + key[i % len(key)]) % permutation_length
            p[i], p[j] = p[j], p[i]

    def __iter__(self):
        return self

    def next(self):
        p = self.permutation
        self.i += 1 
        self.j += p[self.i]
        self.i %= len(p)
        self.j %= len(p)
        p[self.i], p[self.j] = p[self.j], p[self.i]
        return p[(p[self.i] + p[self.j]) % len(p)]

    def encrypt(self, m):
        return m ^ self.next()


def myhex(n):
    r = hex(n)[2:].upper()
    return r if len(r) == 2 else '0' + r


class RC4Tests(unittest.TestCase):
    def test_wikipedia_vectors(self):
        tests = [
                ('Key', 'EB9F7781B734CA72A719', 'Plaintext', 'BBF316E8D940AF0AD3'),
                ('Wiki', '6044DB6D41B7', 'pedia', '1021BF0420'),
                ('Secret', '04D46B053CA87B59', 'Attack at dawn', '45A01F645FC35B383552544B9BF5'),
        ]
        for k, ks, p, c in tests:
            rck = RC4KeyStream(k)
            myks = ''.join([myhex(rck.next()) for __ in xrange(len(ks)/2)])
            print myks, ks
            self.assert_(myks == ks, 'Generated key stream is not equal to correct test value for key=' + k)

        print "Key generation passes tests."

        for k, ks, p, c in tests:
            rck = RC4KeyStream(k)
            myc = ''.join([myhex(rck.encrypt(ord(t))) for t in p])
            print myc, c 
            self.assert_(myc == c, 'Generated cipher is not equal to correct test value for key=' + k)


if __name__ == '__main__':
    unittest.main()

