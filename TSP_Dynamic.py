def tsp(graph, start):
    n = len(graph)
    max_distance = float('inf')
    memo = {}
    shortest_path = []

    def dfs(node, visited, path):
        if visited == (1 << n) - 1:
            path.append(start)
            return graph[node][start], path.copy()
        
        if (node, visited) in memo:
            return memo[(node, visited)]

        min_distance = max_distance
        optimal_path = []

        for next_node in range(n):
            if not visited & (1 << next_node):
                distance, temp_path = dfs(next_node, visited | (1 << next_node), path + [next_node])
                distance += graph[node][next_node]
                
                if distance < min_distance:
                    min_distance = distance
                    optimal_path = temp_path

        memo[(node, visited)] = (min_distance, optimal_path)
        return min_distance, optimal_path

    distance, path = dfs(start, 1 << start, [start])

    return distance, path


n = int(input("Enter the number of cities: "))

print("Enter the distances between cities (use space-separated values):")
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start_node = int(input("Enter the start city (0-indexed): "))

print("\nDistances between cities:")
for row in graph:
    print(row)

distance, path = tsp(graph, start_node)

print("\nMinimum distance for TSP:", distance)
print("Optimal path:", path)

