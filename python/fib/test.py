from __future__ import print_function

from time import time
import math

import fib_closed
import fib_recursive
import fib_memoized
import fib_dynamic
import fib_matrix


def time_it(func, *args, **kwargs):
    start_time = time()
    val = func(*args, **kwargs)
    execution_time = time() - start_time
    return val, execution_time


def test_all():
    for k in range(5, 22):
        print('n = 2 ** {}'.format(k))
        implementations = [fib_closed, fib_matrix, fib_dynamic, fib_memoized]
        if k < 6:
            implementations.append(fib_recursive)
        for module in implementations:
            print('Trying {}:\t'.format(module.__name__), end='')
            try:
                v, e = time_it(module.fib, 2 ** k)
                print('fib(n) has {} digits, took {:.05f} seconds.'.format(
                      int(math.log(v, 10)) + 1, e))
            except Exception as e:
                print(e)
        print('---')


def main():
    n = 10 ** 6
    print('n = 10 ** 6')
    implementations = [fib_matrix, fib_dynamic]
    for module in implementations:
        print('Trying {}:\t'.format(module.__name__), end='')
        try:
            v, e = time_it(module.fib, n)
            print('fib(n) has {} digits, took {:.05f} seconds.'.format(
                  int(math.log(v, 10)) + 1, e))
        except Exception as e:
            print(e)
    print('---')


if __name__ == '__main__':
    main()
