import timeit
import sys
import numpy as np
from Lab2 import *
fin =  open(sys.argv[1])
sizes = [int(i) for i in fin.readline().split()]
runs = int(fin.readline())

RANGE = 1000000                   # Max size of an element (+ or -)
print("Sizes:", sizes)
print("Runs:", runs)
print("Iterations:", ITERATIONS)
print("Range: -"+ str(RANGE) +" to "+ str(RANGE) )

def testOne(A):
  Times = []
    Times.add(timeit.timeit('np.median(A)', number=100)