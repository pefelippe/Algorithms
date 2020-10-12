import sys
import heapq
from collections import OrderedDict
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxsize    
        self.visited = False  
        self.previous = None

    def add_neighbor(self, neighbor, weight):
        self.adjacent[neighbor] = weight
    
    def get_id(self):
        return self.id

    def get_neighbors(self):
        return self.adjacent

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def get_distance(self):
        return self.distance

    def get_previous(self):
        return self.previous

    def set_distance(self, dist):
        self.distance = dist

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True
    
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph():
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def add_vertex(self, v):
        self.num_vertices = self.num_vertices + 1
        vertex = Vertex(v)
        self.vert_dict[v] = vertex
        return vertex

    def add_edge(self, i, f, w=0):
        i.add_neighbor(f, w)

    def get_vertice_by_id(self, id):
        return self.vert_dict[id]

    def printSolution(self): 
        for v in range(self.vert_dict): 
            print ("vertex: " + v + " - distance: " + v.distance) 

    def get_dict(self):
        return self.vert_dict

def sortDict(G, S): 
    #sorted_x = sorted(V.items(), key = lambda x: G.get_vertice_by_id(x[1]).distance) # sort the "vert_dict" by vertex distance
    #return collections.OrderedDict()
    V = G.get_dict()
    D = G.get_dict() - S.items()
    dictOrd =  OrderedDict([(el, V[el]) for el in D]) # falta ordernar pela distancia
    dictOrd = sorted(dictOrd.distance.items())
    return dictOrd
def extractMin(G, V):
    print(V)
    print(type(V))
    deleted = V.popitem(False) # removes the min-vertex from dict
    print(deleted)
    #return G.get_vertice_by_id(deleted[0]) # find vertice by the 'key'
     
def relax(u, v):
    distanceU = u.get_distance()
    distanceV = v.get_distance()
    w = u.get_weight(v) # and if we get two edges from (u->v) ?

    if (distanceU > distanceV + w):
        u.set_distance(distanceV)
        u.set_previous(v)

def printSolution(S):
    print("DISTANCES")
    for i in S:
        print(i.distance)

def dijkstra(G, s):
    print ("Dijkstra's shortest path")
    s.distance = 0
    S = {}
    Q = sortDict(G, S)
    while (len(Q) > 0):
        u = extractMin(G, Q)
        S[u] = u
        for v in u.get_neighbors():
            relax(u, v)
        Q = sortDict(G, S)
    
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