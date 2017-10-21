from buildGraphs import *
import pickle


if len(sys.argv) < 2:
    print("Please include a file")
    exit()


graph = pickle.load( open(sys.argv[1], "rb") )

hist_in = {}
hist_out = {}
for n in graph:
    if hist_in.get(graph[n].inDegree) == None:
        hist_in[graph[n].inDegree] = 1
    else:
        hist_in[graph[n].inDegree] += 1

for n in graph:
    if hist_out.get(graph[n].outDegree) == None:
        hist_out[graph[n].outDegree] = 1
    else:
        hist_out[graph[n].outDegree] += 1

        
print("inDegree:")        
for i in sorted(hist_in.items()):
    print(i)



print("outDegree:")
for i in sorted(hist_out.items()):
    print(i)
    
    
