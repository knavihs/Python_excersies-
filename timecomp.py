'''define two functions f1 and f2 such that,
f1 returns a list of squares of first 20 natural numbers using list comprehension.
f2 returns a generator that computes squares of first 20 natural numbers.
Determine the time taken by each function to get executed 100000 times. Print the time for each function in separate lines.'''

import timeit


def f1():
    f = [i ** 2 for i in range(1, 21)]
    return f


def f2():
    g = (x ** 2 for x in range(1, 21))
    yield g


s1 = timeit.timeit(stmt="f1()", setup="from __main__ import f1", number=100000)
print(s1)
s2 = timeit.timeit(stmt="f2()", setup="from __main__ import f2", number=100000)
print(s2)