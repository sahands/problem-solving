from utils.decorators import memoize


@memoize
def collatz_length(n):
    if n % 2 == 0:
        return 1 + collatz_length(n // 2)
    else:
        if n == 1:
            return 1
        return 1 + collatz_length(3 * n + 1)


def collatz(n):
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        yield n
