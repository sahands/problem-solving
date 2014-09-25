def abs(n):
    return n if n>0 else -n

def cnt(v, d, isfirst):
    print v, d, isfirst
    if d == 0 and v == 0:
        return 1
    if v < 0 or v >= d * 20:
        return 0
    if d == 1:
        return 1 if (v % 2 == 0) else 0
    r = 0
    p = v % 10
    while p < 20:
        r += ((10-abs(p-9)) - isfirst) * cnt((v - p*d - p) / 10, d/100, 0)
        isfirst = 0
        p += 10
    return r

def count(v):
    r = 0
    d = 1
    while d <= v + 1:
        r += cnt(v, d, 1)
        print r
        d *= 10
    return r;

print count(121)
