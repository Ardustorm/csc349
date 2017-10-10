import timeit
from lab2 import *

N=1234568

def setup(n):
    np.random.seed(12357890)
    return np.random.randint(10000, size=n)

def medRandW(A):
    return medSort(A, 0, len(A)-1)
    # return medRand(A, 0, len(A)-1)

print( timeit.timeit("medRandW(lst)",
                                   setup="from __main__ import setup, medRandW \nlst=setup({size})".format( size=N), number=1) , ", ", end='', flush=True)
