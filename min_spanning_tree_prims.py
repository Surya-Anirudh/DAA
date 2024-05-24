import heapq

class PrimGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = [[] for _ in range(num_vertices)]

    def add_edge(self, u, v, weight):
        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))

    def prim(self):
        min_wire_length_a = 0
        min_wire_length_b = 0
        optimal_path_a = []
        optimal_paths_b = []

        visited = [False] * self.num_vertices
        min_heap = [(0, 0, -1)]  # (weight, vertex, parent)

        while min_heap:
            weight, vertex, parent = heapq.heappop(min_heap)

            if visited[vertex]:
                continue
            
            visited[vertex] = True

            if parent != -1:
                optimal_path_a.append((parent, vertex))
                min_wire_length_a += weight

            subtree_length = 0
            optimal_path = []
            for neighbor, edge_weight in self.adjacency_list[vertex]:
                if not visited[neighbor]:
                    heapq.heappush(min_heap, (edge_weight, neighbor, vertex))
                    subtree_length += edge_weight
                    optimal_path.append((vertex, neighbor))
            min_wire_length_b += subtree_length
            optimal_paths_b.append(optimal_path)

        return min_wire_length_a, min_wire_length_b, optimal_path_a, optimal_paths_b

N = int(input("Enter the number of devices: "))
connections = []

print("Enter connections (format: device1 device2 length), type 'done' to finish:")
while True:
    connection_input = input().strip().split()
    if connection_input[0] == 'done':
        break
    u, v, w = map(int, connection_input)
    connections.append((u, v, w))

graph = PrimGraph(N)
for u, v, w in connections:
    graph.add_edge(u - 1, v - 1, w)

total_length_a, total_length_b, optimal_path_a, optimal_paths_b = graph.prim()

print("Minimum length of wire for (a):", total_length_a)
print("Optimal path for (a):", optimal_path_a)
print("Minimum length of wire for (b):", total_length_b)
print("Optimal paths for (b):", optimal_paths_b)
