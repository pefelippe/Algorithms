import sys

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