from buildGraphs import *
import pickle
from queue import Queue
import math

if len(sys.argv) < 2:
    print("Please include a file")
    exit()


graph = pickle.load( open(sys.argv[1], "rb") )



def bfs(start):

    for v in graph.values():
        v.color = WHITE
        v.d = math.inf
        v.pi = None
        
    Q = Queue()

    graph[start].color=GRAY
    graph[start].d=0

    Q.put(graph[start])

    while not Q.empty():
        u = Q.get()
        for vWord in u.adj:
            v = graph[vWord]
            if v.color == WHITE:
                v.d = u.d + 1
                v.pi = u
                v.color = GRAY
                Q.put(v)
        u.color=BLACK



##### Generate list of canidates for start




print("outDegree:")
for n in reversed(sorted(graph.values())):
    if n.outDegree > 800:
        print(n.outDegree, n.word)
        bfs(n.word)
        total=0
        for v in graph.values():
            if v.d != math.inf:
                total += v.d

        print("TOTAL: ", total)
    #bfs search to find dist to each, then sum
    
    
