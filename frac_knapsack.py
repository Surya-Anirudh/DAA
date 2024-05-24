def value_per_weight(item):
    return item[1] / item[0]

def fractional_knapsack(items, capacity):
    items.sort(key=value_per_weight, reverse=True)
    max_value = 0
    solution_vector = [0] * len(items)

    for i, (weight, value) in enumerate(items):
        if capacity == 0:
            break
        if weight <= capacity:
            max_value += value
            solution_vector[i] = 1
            capacity -= weight
        else:
            fraction = capacity / weight
            max_value += value * fraction
            solution_vector[i] = fraction
            capacity = 0

    return max_value, solution_vector

num_items = int(input("Enter the number of items: "))
items = []

for i in range(num_items):
    weight = int(input(f"Enter the weight for item {i+1}: "))
    profit = int(input(f"Enter the value for the item {i+1}: "))
    items.append((weight, profit))

capacity = int(input("Enter the capacity of the Knapsack: "))
max_profit, solution_vector = fractional_knapsack(items, capacity)

print("Maximum profit: ", max_profit)
print("Solution vector: ", solution_vector)
