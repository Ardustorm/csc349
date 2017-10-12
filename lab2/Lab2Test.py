import timeit
import sys
import numpy as np
from lab2 import *

fin =  open(sys.argv[1])
sizes = [int(i) for i in fin.readline().split()]
runs = int(fin.readline())

RANGE = 1000000                   # Max size of an element (+ or -)
ITERATIONS = 100
functions = ['numpy', 'medSortW', 'medRandW', 'medFastW3', 'medFastW5', 'medFastW7']      # Name of functions to test

print("Sizes:", sizes)
print("Runs:", runs)
print("Iterations:", ITERATIONS)
print("Range: -"+ str(RANGE) +" to "+ str(RANGE) )


def setup(n):
    np.random.seed(12357890)
    return np.random.randint(RANGE, size=n)



def numpy(A):
    return np.median(A)

def medSortW(A):
    return medSort(A, 0, len(A)-1)

def medRandW(A):
    return medRand(A, 0, len(A)-1)
    
def medFastW3(A):
    return medFast(A, 0, len(A)-1, 3)
def medFastW5(A):
    return medFast(A, 0, len(A)-1, 3)
def medFastW7(A):
    return medFast(A, 0, len(A)-1, 3)


print



for N in sizes:
    #Heading Stuff
    print("\n\n")
    print("Array Size = ", N)
    print("\n")
    print("function name, average, standard deviation")
    for func in functions:
        print(func, ", ",  end ='')
        times = []
        for i in range(runs):
            
            times.append( timeit.timeit("{func}(lst)".format(func=func),
                                   setup="from __main__ import setup, {func} \nlst=setup({size})".format(func=func, size=N), number=1))
        print(np.mean(times), ", ", np.std(times))
        


