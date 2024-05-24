import math
maxsize = float('inf')

def copyToFinal(curr_path):
    final_path[:N + 1] = curr_path[:]
    final_path[N] = curr_path[0]

def firstMin(adj, i):
    min_val = maxsize
    for k in range(N):
        if adj[i][k] < min_val and i != k:
            min_val = adj[i][k]
    return min_val

def secondMin(adj, i):
    first, second = maxsize, maxsize
    for j in range(N):
        if i == j:
            continue
        if adj[i][j] <= first:
            second = first
            first = adj[i][j]
        elif adj[i][j] <= second and adj[i][j] != first:
            second = adj[i][j]
    return second

def TSPRec(adj, curr_bound, curr_weight, level, curr_path, visited):
    global final_res
    if level == N:
        if adj[curr_path[level - 1]][curr_path[0]] != 0:
            curr_res = curr_weight + adj[curr_path[level - 1]][curr_path[0]]
            if curr_res < final_res:
                copyToFinal(curr_path)
                final_res = curr_res
        return

    for i in range(N):
        if adj[curr_path[level-1]][i] != 0 and not visited[i]:
            temp = curr_bound
            curr_weight += adj[curr_path[level - 1]][i]

            if level == 1:
                curr_bound -= (firstMin(adj, curr_path[level - 1]) + firstMin(adj, i)) / 2
            else:
                curr_bound -= (secondMin(adj, curr_path[level - 1]) + firstMin(adj, i)) / 2

            if curr_bound + curr_weight < final_res:
                curr_path[level] = i
                visited[i] = True
                TSPRec(adj, curr_bound, curr_weight, level + 1, curr_path, visited)

            curr_weight -= adj[curr_path[level - 1]][i]
            curr_bound = temp
            visited = [False] * len(visited)
            for j in range(level):
                if curr_path[j] != -1:
                    visited[curr_path[j]] = True

def TSP(adj, start_city):
    curr_bound = 0
    curr_path = [-1] * (N + 1)
    visited = [False] * N

    for i in range(N):
        curr_bound += (firstMin(adj, i) + secondMin(adj, i))
    curr_bound = math.ceil(curr_bound / 2)

    visited[start_city] = True
    curr_path[0] = start_city
    TSPRec(adj, curr_bound, 0, 1, curr_path, visited)

N = int(input("Enter the number of cities: "))
adj = []
print("Enter the distance between cities in the form adjacency matrix (separate elements by space):")
for _ in range(N):
    row = list(map(int, input().split()))
    adj.append(row)

start_city = int(input("Enter the index of the starting city (0 to N-1): "))

final_path = [None] * (N + 1)
visited = [False] * N
final_res = maxsize

TSP(adj, start_city)

print("Minimum distance for TSP:", final_res)
print("Optimal Path:", end=' ')
for i in range(N + 1):
    print(final_path[i], end=' ')
