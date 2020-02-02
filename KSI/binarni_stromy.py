class Node:
    def __init__(self, key, right=None, left=None):
        self.key = key
        self.right = right
        self.left = left

class Tree:
    def __init__(self, root=None):
        self.root = root

def search(tree, value):
    return find_node(tree.root, value)


def find_node(node, value):
    if not node:
        return False
    if node.key == value:
        return True
    else:
        if node.left or node.right:
            if value > node.key:
                return find_node(node.right, value)
            else:
                return find_node(node.left, value)
        return False

# -----Vzorovy test-----
# Strom:
#        3
#      /   \
#     2     5
#    /    /   \
#   1    4     7
#             /
#            6


node2 = Node(2)
node5 = Node(5)
node8 = Node(8)
node10 = Node(10)
node11 = Node(11)
node12 = Node(12)
node15 = Node(15)
node17 = Node(17)
node18 = Node(18)
node20 = Node(20)
node23 = Node(23)
node31 = Node(31)

node15.left = node8
node15.right = node20
node8.left = node5
node8.right = node11
node5.left = node2
node11.left = node10
node11.right = node12
node20.left = node18
node20.right = node31
node18.left = node17
node31.left = node23


T = Tree(node15)

print(search(T, 8))  # False
print(search(T, 2))  # True
print(search(T, 12))  # True

