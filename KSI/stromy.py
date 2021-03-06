class Tree:
    def __init__(self, root):
        self.root = root

    def  add(self, subtree):
        self.root.children.append(subtree)

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []

# Implementuj funkci, která pro libovolný strom na vstupu vrátí počet jeho uzlů.
def count_nodes(tree):
    return node_count(tree.root, 0)


def node_count(node, counter):
    if not node:
        return 0
    res = counter
    if node.children:
        for i in node.children:
            res += node_count(i, counter)
    return res + 1

# Testy:
print(count_nodes(Tree(None))) # 0
print(count_nodes(Tree(Node(10)))) # 1
print(count_nodes(Tree(Node(5, [Node(6), Node(17)])))) #3
