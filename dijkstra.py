import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def dijkstra(self, src):
        dist = [float("inf")] * self.V
        dist[src] = 0
        pq = [(0, src)]  # Priority queue

        while pq:
            cost, u = heapq.heappop(pq)
            if cost > dist[u]:
                continue
            for v, w in self.graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        self.print_solution(dist)

    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))


# User input for graph definition
V = int(input("Enter the number of vertices: "))
E = int(input("Enter the number of edges: "))

g = Graph(V)

print("Enter the edges (source, destination, weight):")
for _ in range(E):
    u, v, w = map(int, input().split())
    g.add_edge(u, v, w)

source_vertex = int(input("Enter the source vertex: "))
g.dijkstra(source_vertex)
