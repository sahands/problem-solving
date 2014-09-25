import time
from utils.decorators import cached, dump_closure


if __name__ == "__main__":
    @cached(10, True)
    def fib(n):
        """Returns the n'th Fibonacci number."""
        if n == 0 or n == 1:
            return 1
        return fib(n - 1) + fib(n - 2)

    dump_closure(fib)

    print "Testing a function call."
    print "Testing - F(4) = %d" % fib(4)

    @cached(2, True)
    def cached_time():
        return time.time()

    for i in xrange(5):
        print cached_time()
        time.sleep(1)
