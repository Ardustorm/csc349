import timeit
import sys
import numpy as np
from Lab1 import *
fin =  open(sys.argv[1])
sizes = [int(i) for i in fin.readline().split()]
runs = int(fin.readline())

RANGE = 1000000                   # Max size of an element (+ or -)
ITERATIONS = 100
functions = ['numpy', 'multIter', 'multDCWrapper', 'strassenWrapper']      # Name of functions to test
print("Sizes:", sizes)
print("Runs:", runs)
print("Iterations:", ITERATIONS)
print("Range: -"+ str(RANGE) +" to "+ str(RANGE) )


def setup(runs):
    np.random.seed(12357890)
    arrays = [(randMatr(N),randMatr(N))
              for i in range(runs)]
    return arrays


def numpy(n, a, b):
    return np.matmul(a,b)

def multDCWrapper(n, A, B):
    return multDC(n,(0,n), (0,n), (0,n), (0,n), A, B)

def strassenWrapper(n,A,B):
    return multStrassen(n,(0,n), (0,n), (0,n), (0,n), A, B)

for N in sizes:
    #Heading Stuff
    print("\n\n" + "="*60)
    print("Array Size = ", N)
    print("="*60)

    for func in functions:
        print(func)
        total=0
        for i in range(runs):
            #print("from __main__ import {} \narrays=setup({})".format(setup", ".join(functions), runs ))
            total += timeit.timeit("{}({}, arrays[{}][0], arrays[{}][1])".format(func,N, i,i),
                                   setup="from __main__ import setup, {} \narrays=setup({})".format(", ".join(functions), runs), number=runs)
        print(total)

