from queue import PriorityQueue

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
class Node:
    def __init__(self, level, profit, weight, includes):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.includes = includes
    def __lt__(self, other):
        return other.weight - self.weight
    
def bound(u, n, W, arr):
    if u.weight >= W:
        return 0
    profit_bound = u.profit
    j = u.level + 1
    total_weight = u.weight
    while j < n and total_weight + arr[j].weight <= W:
        total_weight += arr[j].weight
        profit_bound += arr[j].value
        j += 1
    if j < n:
        profit_bound += int((W - total_weight) * arr[j].value / arr[j].weight)
    return profit_bound

def knapsack(W, arr, n):
    arr.sort(key=lambda x: x.value / x.weight, reverse=True)
    priority_queue = PriorityQueue()
    u = Node(-1, 0, 0, [])
    priority_queue.put(u)
    max_profit = 0
    best_node = None

    while not priority_queue.empty():
        u = priority_queue.get()
        if u.level == -1:
            v = Node(0, 0, 0, [])
        elif u.level == n - 1:
            continue
        else:
            v = Node(u.level + 1, u.profit, u.weight, u.includes[:])

        if v.level < n:
            v.weight += arr[v.level].weight
            v.profit += arr[v.level].value
            v.includes.append(v.level)

            if v.weight <= W and v.profit > max_profit:
                max_profit = v.profit
                best_node = v

            v_bound = bound(v, n, W, arr)
            if v_bound > max_profit:
                priority_queue.put(v)

            v = Node(u.level + 1, u.profit, u.weight, u.includes[:])
            v_bound = bound(v, n, W, arr)
            if v_bound > max_profit:
                priority_queue.put(v)

    return max_profit, best_node


W = int(input("Enter the Maximum Weight Capacity of the Knapsack: "))
n = int(input("Enter the Number of Items: "))
weights = list(map(float, input("Enter the Weights of the Items separated by spaces: ").split()))
values = list(map(float, input("Enter the Values of the Items separated by spaces: ").split()))
arr = [Item(weights[i], values[i]) for i in range(n)]
max_profit, best_node = knapsack(W, arr, n)
solution_vector = [0] * n
if best_node:
    for idx in best_node.includes:
        solution_vector[idx] = 1
print("Maximum  Profit =", max_profit)
print("Solution Vector :", solution_vector)
