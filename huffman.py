# import heapq

# class Node:
#     def __init__(self, freq, symbol, left=None, right=None):
#         self.freq = freq
#         self.symbol = symbol
#         self.left = left
#         self.right = right
#         self.huff = ''

#     def __lt__(self, nxt):
#         return self.freq < nxt.freq

# def printNodes(node, val=''):
#     newVal = val + str(node.huff)
#     if (node.left):
#         printNodes(node.left, newVal)
#     if (node.right):
#         printNodes(node.right, newVal)
#     if not node.left and not node.right:
#         print(f"{node.symbol} -> {newVal}")

# def build_huffman_tree(chars, freq):
#     nodes = []
#     for x in range(len(chars)):
#         heapq.heappush(nodes, Node(freq[x], chars[x]))
#     while len(nodes) > 1:
#         left = heapq.heappop(nodes)
#         right = heapq.heappop(nodes)
#         left.huff = '0'
#         right.huff = '1'
#         newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
#         heapq.heappush(nodes, newNode)
#     return nodes[0]

# chars = input("Enter Characters Separated By Spaces: ").split()
# freq = list(map(int, input("Enter Corresponding Frequencies Separated By Spaces: ").split()))

# root_node = build_huffman_tree(chars, freq)
# print("Huffman Codes:")
# printNodes(root_node)

# Huffman Coding in python


string = input("Enter the String: ")

class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d

freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])

print(' Char | Huffman code ')
print('----------------------')
for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, huffmanCode[char]))