import sys

sys.path.insert(0, './lib')

from Graph import *

import heapq

from collections import OrderedDict

def createHeap(G): # nlogn (i guess)
    sorted_x = sorted(G.vert_dict.items(), key = lambda x:
                                                G.get_vertice_by_id(x[0]).distance) # sort the "vert_dict" by vertex distance
    
    return OrderedDict(sorted_x)

def extractMin(G, D): 
    vertex = D.popitem(last=False)
    u = G.get_vertice_by_id(vertex[0])
    return u, D
    
def relaxEdge(u, v):
    distanceU = u.get_distance()
    distanceV = v.get_distance()
    w = u.get_weight(v)
    
    if (distanceU + w < distanceV):
        v.set_distance(int(distanceU) + int(w))
        v.set_previous(u)

    
def mantemHeap(S):
    print('actualize heap')

def printSolution(S):
    print("DJIKSTRA ALGORITHM")
    for i in S:
        print('----------------------------------------------')
        print(f' Vertex: |{i.id}| - Distance from source: |{i.distance}|') 
    
    print('----------------------------------------------')
    
def dijkstra(G, s):
    s.distance = 0
    S = {}
    S[s] = s
    Q = createHeap(G) 
    
    while (len(Q) > 1):
        u, Q = extractMin(G, Q)
        S[u] = u
        for neighbour in u.get_neighbors():
            relaxEdge(u, neighbour)
        
    printSolution(S)

if __name__ == '__main__':

    g = Graph()

    a = g.add_vertex('a')
    b = g.add_vertex('b')
    c = g.add_vertex('c')
    d = g.add_vertex('d')
    e = g.add_vertex('e')
    f = g.add_vertex('f')

    g.add_edge(a, b, 7)  
    g.add_edge(a, b, 6)
    g.add_edge(a, f, 14)
    g.add_edge(b, c, 10)
    g.add_edge(b, d, 15)
    g.add_edge(c, d, 11)
    g.add_edge(c, f, 2)
    g.add_edge(d, e, 6)
    g.add_edge(e, f, 9)

    dijkstra(g, a)