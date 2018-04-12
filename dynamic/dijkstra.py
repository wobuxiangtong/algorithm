import sys
class Graph(object):
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def printSolution(self,dist):
        print("Vertex tDistance from source")
        for node in range(self.V):
            print(node,"t",dist[node])

    def minDistance(self,dist,sptSet):
        min = sys.maxsize
        min_index = 0
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index
    def findroad(self,roads,u,v):
        new_roads = roads.copy()
        for _,item in roads.items():
            if item[-1] == str(u):
                new_roads[v] = item + str(v)
        return new_roads

    def dijkstra(self,src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        roads = {src : str(src)}
        for _ in range(self.V):
            u = self.minDistance(dist,sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    roads = self.findroad(roads,u,v)
        self.printSolution(dist)
        print(roads)


g = Graph(6)

g.graph = [
            [0,6,3,0,0,0],
            [6,0,2,5,0,0],
            [3,2,0,3,4,0],
            [0,5,3,0,2,3],
            [0,0,4,2,0,5],
            [0,0,0,3,5,0]
            ]
g.dijkstra(0)



