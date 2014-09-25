from cached import cached
from dump_closure import dump_closure


@cached(10, True)
def fib(n):
    """Returns the n'th Fibonacci number."""
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

dump_closure(fib)

print "Testing a function call."
print "Testing - F(4) = %d" % fib(4)
