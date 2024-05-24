class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        self.print_solution(dist)

    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))


# User input for graph definition
V = int(input("Enter the number of vertices: "))
E = int(input("Enter the number of edges: "))

g = Graph(V)

print("Enter the edges (source, destination, weight separated by space):")
for _ in range(E):
    u, v, w = map(int, input().split())
    g.add_edge(u, v, w)

source_vertex = int(input("Enter the source vertex: "))
g.bellman_ford(source_vertex)
