import cProfile


def f1():
    f = [i ** 2 for i in range(1, 20001)]
    return f


def f2():
    g = (x ** 2 for x in range(1, 20001))
    yield g

s1= cProfile.runctx( "f1()", globals(),locals() )
print(s1)
s2 = cProfile.runctx( "f2()", globals(),locals() )
print(s2)