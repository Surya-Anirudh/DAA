class DisjointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

def kruskal(N, connections):
    connections.sort(key=lambda x: x[2])  
    ds = DisjointSet(N)
    min_wire_length_a = 0
    min_wire_length_b = 0
    optimal_path_a = []  
    optimal_paths_b = []  

    for u, v, w in connections:
        if ds.union(u-1, v-1):
            min_wire_length_a += w
            optimal_path_a.append((u, v))

    for i in range(N):
        ds = DisjointSet(N)
        subtree_length = 0
        optimal_path = []  
        for u, v, w in connections:
            if (u == i+1 and v == 1) or (u == 1 and v == i+1):
                continue
            if ds.union(u-1, v-1):
                subtree_length += w
                optimal_path.append((u, v))
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
total_length_a, total_length_b, optimal_path_a, optimal_paths_b = kruskal(N, connections)
print("Minimum length of wire for (a):", total_length_a)
print("Optimal path for (a):", optimal_path_a)
print("Minimum length of wire for (b):", total_length_b)
print("Optimal paths for (b):", optimal_paths_b)


