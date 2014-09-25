import sys

for line in sys.stdin:
    n, b, t = [int(x) for x in line.split()]
    bp, tp = 0, 0
    bob, ted = 0, 0
    # print "--"
    while n > 0 or tp >0 or bp >0:
        # print n, bob, ted, bp, tp
        if bp == 0 and tp == 0:
            x = min(n, b)
            bp += x
            n -= x
            x = min(n, t)
            tp += x
            n -= x
            if bp > 0:
                bp -= 1
                bob += 1
            if tp > 0:
                tp -= 1
                ted += 1
        elif bp == 0:
            x = min(n, b)
            bp += x
            n -= x
            if tp > 0:
                tp -= 1
                ted += 1
        elif tp == 0:
            x = min(n, t)
            tp += x
            n -= x
            if bp > 0:
                bp -= 1
                bob += 1
        else:
            if bp > 0:
                bp -= 1
                bob += 1
            if tp > 0:
                tp -= 1
                ted += 1

    print "{0} {1}".format(bob, ted)
