def F():
    a,b = 0,1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b

f = F()
f.next()
f.next()
for i in xrange(2,41):
    print '+-----------+-------------+-------------------------------+'
    print '| %d         | %d           |                               |' % (i, f.next()) 

