from mathutils.collatz import collatz

ml = 0
mn = 0
for n in xrange(10 ** 6):
    l = len(list(collatz(n)))
    if l > ml:
        ml = l
        mn = n
    print n, l

print mn, ml

