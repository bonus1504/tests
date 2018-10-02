from itertools import tee, accumulate
from operator import mul
from functools import reduce
import timeit


def func():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


t, s = tee(func())
pairs = zip(t, accumulate(s))

for _, (fib, acc) in zip(range(10), pairs):
    print(fib, acc)


def fact(n):
    return reduce(mul, range(1, n+1), 1)


if __name__ == '__main__':
    #print(fact(1000))
    t = timeit.Timer('fact(1000)', setup='from __main__ import fact')
    print(t.timeit(number=1000))
