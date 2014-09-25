def fib(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a
