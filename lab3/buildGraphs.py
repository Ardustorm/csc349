import pickle
import sys
import csv

class Node:
    def __init__(self, adjNode):
        self.adj = {}
        self.update(adjNode)
        self.degree = 1
    def update(self, adjNode):
        node = self.adj.get(adjNode)
        self.degree += 1
        if node == None:
            self.adj[adjNode] = 1
        else:
            self.adj[adjNode] += 1




class Graph:
    digraph = {}
    ungraph = {}
    def __init__(self, filename):
        csvReader = csv.reader( open(filename) )
        for row in csvReader:

            #### un-Directed graph ########
            if self.ungraph.get(row[1]) == None:
                self.ungraph[row[1]] = Node(row[2])
            else:
                self.ungraph[row[1]].update(row[2])

            if self.ungraph.get(row[2]) == None:
                self.ungraph[row[2]] = Node(row[1])
            else:
                self.ungraph[row[2]].update(row[1])

                
            ##### DIRECTED Graph ######
            if self.digraph.get(row[1]) == None:
                self.digraph[row[1]] = Node(row[2])
            else:
                self.digraph[row[1]].update(row[2])

    def dump(self):
        pickle.dump( self.digraph, open("directedGraph.weCanReallyChooseAnyExtentionWeWant.p", "wb"))
        pickle.dump( self.ungraph, open("undirectedGraph.weCanReallyChooseAnyExtentionWeWant.p", "wb"))
if len(sys.argv) < 2:
    print("Please include a file")
    exit()

    graph = {}



graph = Graph(sys.argv[1])
graph.dump()
