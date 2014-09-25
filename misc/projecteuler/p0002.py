N = 4 * (10 ** 6)

a = 1
b = 2
n = 0

while a <= N:
    if a % 2 == 0:
        print a
        n += a
    a, b = b, a + b

print n
