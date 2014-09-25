def border_array(x):
    """Calculate the border array (i.e. failure function) of string x."""
    n = len(x)
    beta = [0] * n
    b = 0
    for i in xrange(1, n):
        while b > 0 and x[i] != x[b]:
            b = beta[b - 1]
        beta[i] = b = (b + 1 if x[i] == x[b] else 0)
    return beta


def kmp_search(x, p):
    """
    Return an iterator for all instances of p occurring in x.
    Overlapping matches are allowed. For example kmp_search('ababa', 'aba')
    yields 0 and 2.
    """
    beta = border_array(p)
    print beta
    i = m = 0
    while m + i < len(x):
        if x[m + i] == p[i]:
            if i == len(p) - 1:
                yield m
            else:
                i += 1
                continue
        m, i = (m + i - beta[i - 1], beta[i - 1]) if i > 0 else (m + 1, 0)


def test(s):
    beta = border_array(s)
    print beta
    b = beta[-1]
    print s[:b]
    print s[-b:]

# test('abaababaa')
# test('abaababaa')
# test('abaabaaabaaaabaaaaab')
# test('ababaa')

p = 'abaaabbaabaa'
beta = border_array(p)
print beta
b = beta[-1]
print p[:b], p[-b:]
for i, b in enumerate(beta):
    if b == 0:
        print i, b, '', ''
    else:
        print i, b, p[:b], p[:i + 1][-b:]

exit()
# s = '10110101'
# p = '1101'
s = 'abaaabbaabaababaaabbaabaaba'
p = 'abaaabbaaba'

for m in kmp_search(s, p):
    print m, s[m:m+len(p)]
