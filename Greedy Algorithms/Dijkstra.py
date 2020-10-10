import sys
import heapq

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxint    
        self.visited = False  
        self.previous = None

    def add_neighbor(self, neighbor, weight):
        self.adjacent[neighbor] = weight
    
    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

class Graph():
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0
    
    def printSolution(self, dist): 
        print ("Vertex tDistance from Source") 
        for node in range(self.vert_dict): 
            print (node, "t", dist[node]) 

    def addVertex(self, v):
        self.num_vertices = self.num_vertices + 1
        vertex = Vertex(v)
        self.vert_dict[v] = vertex
        return vertex

    def addEdge(self, i, f, w=0):
        self.vert_dict[i].add_neighbor(self.vert_dict[f], w)

def extractMin(Q):
    return Q.pop()

def relax(u, v):
    if (u.distance > v.distance):
        u.distance = v.distance
        u.previous = v

def dijkstra(G, s):
    print ("Dijkstra's shortest path")
    s.distance = 0
    S = 0 
    Q = G # montar heap
    while (Q != 0):
        u = extractMin(Q)
        S = S + u
        for v in u.adjacent:
            relax(v, u)
    print(S) 
    return S

if __name__ == '__main__':

    g = Graph()

    g.addVertex('a')
    g.addVertex('b')
    g.addVertex('c')
    g.addVertex('d')
    g.addVertex('e')
    g.addVertex('f')

    g.addEdge('a', 'b', 7)  
    g.addEdge('a', 'c', 9)
    g.addEdge('a', 'f', 14)
    g.addEdge('b', 'c', 10)
    g.addEdge('b', 'd', 15)
    g.addEdge('c', 'd', 11)
    g.addEdge('c', 'f', 2)
    g.addEdge('d', 'e', 6)
    g.addEdge('e', 'f', 9)

dijkstra(g)