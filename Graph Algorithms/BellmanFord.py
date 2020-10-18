from Graph import *

def relaxEdge(G, edge):
    
    u,v,w = edge
    u = G.getVertexById(u.getId())
    v = G.getVertexById(v.getId())
    
    distanceU = u.getDistance()
    distanceV = v.getDistance()
    
    if (distanceU + w < distanceV):
        v.setDistance(distanceU + w)

def printSolution(S):
    for v in S.vert_dict:
        i = S.getVertexById(v)
        print('----------------------------------------------')
        print(f' Vertex: |{i.getId()}| - Distance from source: |{i.getDistance()}|') 
    print('----------------------------------------------')

def bellmanFord(G, s):
    print("Bellman-Ford's shortest path")
    s.setDistance(0)
    i = 0
    while(i < (G.num_vertices)):
        for edge in G.edges_list:
            relaxEdge(G, edge)
        i = i + 1
    
    for edge in G.edges_list:
        u,v,w = edge
        if (v.getDistance() > u.getDistance() + w):
            print("NEGATIVE CYCLE")
            return False

    printSolution(G)
    return True

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

    bellmanFord(g, a)