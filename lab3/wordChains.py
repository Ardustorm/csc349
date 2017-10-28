from buildGraphs import *
import pickle
from queue import Queue


if len(sys.argv) < 2:
    print("Please include a file")
    exit()


graph = pickle.load( open(sys.argv[1], "rb") )

start = input("Enter starting word: ")
#start = "magneto"
end = input("Enter ending word: ")
#end = "horrible american beer"

print(start, end)

#bfs
Q = Queue()

graph[start].color=GRAY
graph[start].d=0

Q.put(graph[start])



while not Q.empty():
    u = Q.get()
    # TODO: one of these ways might sort by most used. we should use that one.
    #for vWord in u.adj:
    for vWord in sorted(u.adj, reverse=False):   
        v = graph[vWord]
        if v.color == WHITE:
            v.d = u.d + 1
            v.pi = u
            v.color = GRAY
            Q.put(v)
    u.color=BLACK



stack = [end,]

while graph[ stack[-1] ].pi != None:
    stack.append(graph[ stack[-1] ].pi.word)


while len(stack) > 1:
    print(stack.pop(), ,end= " -> ")
    
print(stack.pop(), "\t[", graph[end].d, "steps ]")
