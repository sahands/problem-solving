import unittest


def f_recursive(m, s, n=0, k=0):
    if k == 0:
        k = max(len(x) for x in m.keys())
    if n == len(s):
        return set([''])
    strings = set()
    for j in range(n + 1, min(len(s) + 1, n + k + 1)):
        key = s[n:j]
        if key in m:
            strings1 = f_recursive(m, s, j, k)
            strings |= set(m[key] + x for x in strings1)
    return strings


def f_dynamic(m, s):
    # Use a dict of sets to keep do dynamic programming
    # d[x] is the set of possible string interpretations for string x
    n = len(s)
    k = max(len(x) for x in m.keys()) 
    d = {'' : set([''])}
    for i in xrange(1,n+1):
        suffix = s[-i:]
        d[suffix] = set()
        for j in xrange(1, min(k+1, i+1)):
            key = suffix[:j]
            if key in m:
                strings = d[suffix[j:]]
                d[suffix] |= set(m[key] + z for z in strings)
    return d[s]


class TestNumbersToLetters(unittest.TestCase):
    def test_main(self):
        s = '1212111'
        m = {'1':'a', '2':'b', '3':'c', '11':'x', '12':'y', '111':'z'}
        s1 =  f_dynamic(m, s)
        s2 =  f_recursive(m, s)
        print s1
        print s2        
        self.assert_(s1 == s2)

       
if __name__ == '__main__':
    unittest.main()
