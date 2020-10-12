import sys
sys.path.insert(0, './lib')

from Graph import *

import heapq

from collections import OrderedDict

def createHeap(G, S): # deve retornar 
    print("Creating Heap")

def extractMin(G, V): # deve retornar um vertice
    print("Extracting")
    
def relax(u, v):
    print("Relaxing")
    distanceU = u.get_distance()
    distanceV = v.get_distance()
    w = u.get_weight(v)

    if (distanceU > distanceV + w):
        u.set_distance(distanceV)
        u.set_previous(v)

def printSolution(S):
    print("RESULTS")
    for i in S:
        print(f'{i.id} - {i.distance}') 

def dijkstra(G, s):
    print ("Dijkstra's shortest path")
    s.distance = 0
    S = {}
    S[s] = s
    Q = createHeap(G)
    
    while (len(Q) > 1):
        u = extractMin(Q)
        S[u] = u
        for neighbour in u.neighbours:
            relax(u, neighbour)
        actualizeHeap(Q)
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
    g.add_edge(a, c, 9)
    g.add_edge(a, f, 14)
    g.add_edge(b, c, 10)
    g.add_edge(b, d, 15)
    g.add_edge(c, d, 11)
    g.add_edge(c, f, 2)
    g.add_edge(d, e, 6)
    g.add_edge(e, f, 9)

    d = dijkstra(g, a)