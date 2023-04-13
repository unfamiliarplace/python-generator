import timeit
import random
from pandas import Series
from numpy import array

_L = [random.randint(1, 1_000) for _ in range(1_000)]

def _plus5(n):
    return n + 5

def loop_build_add(L):
    L2 = []
    for elem in L:
        L2 = L2 + [elem + 5]

def loop_build_increment(L):
    L2 = []
    for elem in L:
        L2 += [elem + 5]

def loop_build_append(L):
    L2 = []
    for elem in L:
        L2.append(elem + 5)

def loop_build_extend(L):
    L2 = []
    for elem in L:
        L2.extend([elem + 5])

def loop_build_zeroes(L):
    L2 = [0] * len(L)
    for i in range(len(L)):
        L2[i] = L[i] + 5

def loop_inplace_add(L):
    for i in range(len(L)):
        L[i] = L[i] + 5

def loop_inplace_increment(L):
    for i in range(len(L)):
        L[i] += 5

def map_gen(L):
    map(_plus5, L)

def map_cast(L):
    list(map(_plus5, L))

def listcomp_gen(L):
    (elem + 5 for elem in L)

def listcomp_cast(L):
    [elem + 5 for elem in L]

def pandas_series(L):
    Series(L) + 5

def pandas_series_cast(L):
    (Series(L) + 5).tolist()

def numpy_array(L):
    array(L) + 5

def numpy_array_cast(L):
    (array(L) + 5).tolist()

methods = [
    loop_build_add,       # takes obnoxiously long, about 1 order of magnitude more
    loop_build_increment,
    loop_build_append,
    loop_build_extend,
    loop_build_zeroes,
    loop_inplace_add,
    loop_inplace_increment,
    map_gen,
    map_cast,
    listcomp_gen,
    listcomp_cast,
    pandas_series,
    pandas_series_cast,
    numpy_array,
    numpy_array_cast
]

for cb in methods:
    result = timeit.timeit(lambda: cb(_L[:]), number=10_000)
    print(f'{cb.__name__: <25}{result:.5f}')
