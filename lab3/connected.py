from buildGraphs import *
import pickle


if len(sys.argv) < 2:
    print("Please include a file")
    exit()


graph = pickle.load( open(sys.argv[1], "rb") )

print(graph["email"].adj)
