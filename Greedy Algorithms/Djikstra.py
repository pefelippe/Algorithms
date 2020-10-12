import sys

sys.path.insert(0, './lib')

from Graph import *

from collections import OrderedDict
#
def createHeap(G): # nlogn (i guess)
    sorted_x = sorted(G.vert_dict.items(), key = lambda x:
                                                G.getVertexById(x[0]).getDistance()) # sort the "vert_dict" by vertex distance
    
    return OrderedDict(sorted_x)

def extractMin(G, D): 
    vertex = D.popitem(last=False)
    u = G.getVertexById(vertex[0])
    return u, D
    
def relaxEdge(G, edge):
    
    u,v,w = edge
    
    u = G.getVertexById(u.getId())
    v = G.getVertexById(v.getId())
    
    distanceU = u.getDistance()
    distanceV = v.getDistance()
    
    if (distanceU + w < distanceV):
        v.setDistance(distanceU + w)

def printSolution(S):

    for i in S:
        print('----------------------------------------------')
        print(f' Vertex: |{i.getId()}| - Distance from source: |{i.getDistance()}|') 
    print('----------------------------------------------')
    
def dijkstra(G, s):
    print("Djikstra's shortest path")
    s.setDistance(0)
    S = {}
    S[s] = s
    Q = createHeap(G) 
    
    while (len(Q) > 1):
        u, Q = extractMin(G, Q)
        S[u] = u
        for edge in u.getEdges():
            relaxEdge(G, edge)
        
    printSolution(S)

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

    dijkstra(g, a)