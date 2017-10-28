from buildGraphs import *
import pickle
from queue import Queue
import math

if len(sys.argv) < 2:
    print("Please include a file")
    exit()


graph = pickle.load( open(sys.argv[1], "rb") )

def BFS(start):
    start.color=GRAY
    start.d=0
    Q = Queue()
    Q.put(start)
    numWords=0
    totDepth=0
    depths={}
    
    while not Q.empty():
        u = Q.get()
        numWords+=1
        totDepth+=u.d
        if depths.get(u.d)==None:
            depths[u.d] = 1
        else:
            depths[u.d]+=1
        #u.inDegree=len(u.adj)
        for vWord in u.adj:
            v = graph[vWord]
            if v.color == WHITE:
                v.d = u.d + 1
                v.pi = u
                v.color = GRAY
                Q.put(v)
        u.color=BLACK
    return [numWords, totDepth, depths]

def initBFS(vals):
  for v in vals:
    v.color = WHITE
    v.d = math.inf
    v.pi = None

def sorter(x):
    return x[3]/x[2]
    
def printData(data):
    for d in data:
        print("\n"+d[0])
        print("  Degree:", d[1])
        #print("  Number of Words:", d[2])
        #print("  Total Depth:", d[3])
        print("  Average Path Length:", d[3]/d[2])
        print("  Hist:", d[4])
 
def main():
    data=[]
    for n in reversed(sorted(graph.values())):
        if n.outDegree > 300:
            initBFS(graph.values())
            data.append([n.word, n.outDegree]+BFS(n))
    data.sort(key=sorter)
    printData(data)
        
    
main()
