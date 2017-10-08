import timeit
from lab2 import *

N=1234568

def setup(n):
    np.random.seed(12357890)
    return np.random.randint(10000, size=n)

print( timeit.timeit("lab2.medRand(lst, 0, 1234567)",
                                   setup="from __main__ import setup, setup \nimport lab2\nlst=setup({size})".format( size=N), number=1) , ", ", end='', flush=True)
