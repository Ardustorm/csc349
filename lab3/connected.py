from buildGraphs import *
import pickle
from queue import Queue
import math

if len(sys.argv) < 2:
    print("Please include a file")
    exit()


graph = pickle.load( open(sys.argv[1], "rb") )
#print(graph["email"].adj)


#takes white starting vertex of inited graph
#returns array [#words, higestDeg, #ofHigestDeg, [wordsOfHighestDeg(<=20)]]
def BFS(start):
    start.color=GRAY
    start.d=0
    Q = Queue()
    Q.put(start)
    numWords=0
    highDeg=0
    numHighDeg=0
    wordsHighDeg=[]
    
    while not Q.empty():
        u = Q.get()
        numWords+=1
        #if u.outDegree!=len(u.adj):
        #    print("----------BROKEN-------------")
        u.inDegree=len(u.adj)
        if u.inDegree > highDeg:
            highDeg=u.inDegree
            numHighDeg=1
            wordsHighDeg=[u.word]
        elif u.inDegree==highDeg:
            numHighDeg+=1
            wordsHighDeg.append(u.word)
        for vWord in u.adj:
            v = graph[vWord]
            if v.color == WHITE:
                v.d = u.d + 1
                v.pi = u
                v.color = GRAY
                Q.put(v)
        u.color=BLACK
        wordsHighDeg.sort()
    return [numWords, highDeg, numHighDeg, wordsHighDeg[0:(20 if len(wordsHighDeg)>=20 else len(wordsHighDeg))]]

def initBFS(vals):
  for v in vals:
    v.color = WHITE
    v.d = math.inf
    v.pi = None
    
def numberWords(x):
    return -x[0]
    
def printData(numComp, D, filter):
  print("Number of Components:", numComp)
  n=0
  D.sort(key=numberWords)
  for comp in D:
    if(comp[0]>filter):
        n+=1
        print("\nComponent:", n)
        print("  Number of Words:", comp[0])
        print("  Highest Degree:", comp[1])
        print("  Number of Highest Degree:", comp[2])
        print("  Words of Highest Degree:\n", comp[3])
  print("\n"+str(len(D)-n)+" Not Shown (Subgraphs with less than 4 words)")

def printData2(numComp, D, thresh):
  print("Number of Components:", numComp)
  n=0
  D.sort(key=numberWords)
  for comp in D:
    if(comp[0]>thresh):
        n+=1
        print("\nComp Num    Words    Highest-Degree    Number    Words")
        print(str(n)+"\t    "+str(comp[0])+"    \t"+str(comp[1])+"\t\t"+str(comp[2])+"\t "+str(comp[3]))    
  print("\n"+str(len(D)-n)+" Not Shown (Subgraphs with less than 4 words)")
  
def main():
  initBFS(graph.values())
  connectedData=[]
  numComp=0

  for n in reversed(sorted(graph.values())):
    if n.color == WHITE:
      connectedData.append(BFS(n))
      numComp+=1
  printData2(numComp, connectedData, 4)
                
main()

