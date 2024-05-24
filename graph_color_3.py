def greedy_coloring(graph):
    result = [-1] * len(graph)
    result[0] = 0
    available = [False] * len(graph)

    for u in range(1, len(graph)):
        for i in graph[u]:
            if result[i] != -1:
                available[result[i]] = True

        color = 0
        while color < len(graph) and available[color]:
            color += 1

        result[u] = color

        for i in graph[u]:
            if result[i] != -1:
                available[result[i]] = False

    chromatic_number = max(result) + 1

    for u in range(len(graph)):
        print(f"Vertex {u} --->  Color {result[u]}")

    return chromatic_number, result

if __name__ == '__main__':
    num_vertices = int(input("Enter the number of vertices: "))
    graph = []

    for i in range(num_vertices):
        edges = input(f"Enter the vertices connected to vertex {i} (separated by spaces): ").split()
        edges = [int(x) for x in edges]
        graph.append(edges)

    print("Coloring of the graph:")
    chromatic_number, coloring_result = greedy_coloring(graph)
    print("Chromatic number:", chromatic_number)
