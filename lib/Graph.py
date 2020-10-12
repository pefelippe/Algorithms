import sys

class Vertex:
    def __init__(self, node):
        self.id = node
        self.edges = []
        self.distance = sys.maxsize    

    def getId(self):
        return self.id

    def getDistance(self):
        return self.distance

    def setDistance(self, dist):
        self.distance = dist
    
    def getEdges(self):
        return self.edges
    
class Graph():
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def addVertex(self, v):
        vertex = Vertex(v)
        self.vert_dict[v] = vertex
        return vertex

    def addEdge(self, i, f, w=0):
        i.edges.append([i, f, w])

    def getVertexById(self, id):
        return self.vert_dict[id]

    def printSolution(self): 
        for v in range(self.vert_dict): 
            print ("vertex: " + v + " - distance: " + v.getDistance()) 
