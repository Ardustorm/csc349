import pickle
import sys
import csv
import math
IN = 0
OUT = 1
WHITE = 0
GRAY = 1
GREY = 1
BLACK = 2
class Node:
    def __init__(self, word, adjNode, degreeDir=OUT):
        self.word = word
        self.pi = None          # parent
        self.d = math.inf
        self.adj = {}
        self.inDegree = 0
        self.outDegree = 0
        self.color = WHITE
        if degreeDir == OUT:
            self.update(adjNode)
        if degreeDir == IN:
            self.adjustInDegree()
            
    def update(self, adjNode):
        if self.adj.get(adjNode) == None:
            self.adj[adjNode] = 1
        else:
            self.adj[adjNode] += 1

        self.outDegree += 1

    def adjustInDegree(self):
        self.inDegree += 1

    def __gt__(self, other):
        return self.outDegree > other.outDegree

class Graph:
    digraph = {}
    ungraph = {}
    def __init__(self, filename):
        csvReader = csv.reader( open(filename) )
        for row in csvReader:

            #### un-Directed graph ########
            if self.ungraph.get(row[1]) == None:
                self.ungraph[row[1]] = Node(row[1], row[2])
            else:
                self.ungraph[row[1]].update(row[2])

            if self.ungraph.get(row[2]) == None:
                self.ungraph[row[2]] = Node(row[2], row[1])
            else:
                self.ungraph[row[2]].update(row[1])

                
            ##### DIRECTED Graph ######
            if self.digraph.get(row[1]) == None:
                self.digraph[row[1]] = Node(row[1], row[2])
            else:
                self.digraph[row[1]].update(row[2])

            if self.digraph.get(row[2]) == None:
                self.digraph[row[2]] = Node(row[2], row[1], IN)
            else:
                self.digraph[row[2]].adjustInDegree()


    def dump(self):
        pickle.dump( self.digraph, open("directedGraph.weCanReallyChooseAnyExtentionWeWant.p", "wb"))
        pickle.dump( self.ungraph, open("undirectedGraph.weCanReallyChooseAnyExtentionWeWant.p", "wb"))


    def test(self):
        pass



if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Please include a file")
        exit()





    graph = Graph(sys.argv[1])
    
    #graph.test()

    graph.dump()
