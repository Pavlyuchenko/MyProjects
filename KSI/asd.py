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
    if node.children:
        for i in node.children:
            counter += node_count(i, counter)
    print(node.value, counter)
    return counter + 1

# Testy:
print(count_nodes(Tree(Node(1, [Node(2), Node(5)])))) #3
