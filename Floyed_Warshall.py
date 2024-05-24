nV = int(input("Enter the number of vertices: "))
INF = float('inf')

def floyd_warshall(G):
    distance = [[INF] * nV for _ in range(nV)]

    for i in range(nV):
        for j in range(nV):
            if i == j:
                distance[i][j] = 0
            elif G[i][j] != INF:
                distance[i][j] = G[i][j]

    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)

def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if distance[i][j] == INF:
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print()

G = []
print("Enter the adjacency matrix for the graph (use 'INF' for infinity):")
for i in range(nV):
    row = input().split()
    G.append([INF if x == 'INF' else int(x) for x in row])

print("Adjacency Matrix of All Pair Shortest Paths is  ")
floyd_warshall(G)
