# All Pairs Shortest Path (Floyd-Warshall) - Dynamic Programming
# Complexity: O (N^3)

from Graph import *

def initializeMatrix(M, G):


def calculateAllPairsShortestPath(M, V):
    for k in range(len(V)):
        for i in range(len(V)):
            for j in range(len(V)):
                if (M[i,j] > M[i, k] + M[k,j]):
                    M[i,j] = M[i, k] + M[k,j]
                    
                    
if __name__ == '__main__':

    g = Graph()

    a = g.addVertex('a')
    b = g.addVertex('b')
    c = g.addVertex('c')
    d = g.addVertex('d')
    e = g.addVertex('e')
    f = g.addVertex('f')

    g.addEdge(a, b, 6) 
    g.addEdge(a, b, 7)  
    g.addEdge(a, f, 14)
    g.addEdge(b, c, 10)
    g.addEdge(b, d, 15)
    g.addEdge(c, d, 11)
    g.addEdge(c, f, 2)
    g.addEdge(d, e, 6)
    g.addEdge(e, f, 9)

    num_vertex = g.num_vertices
    
    M = [[0], []] 
    V = g.vert_dict
    
    calculateAllPairsShortestPath(M, V)