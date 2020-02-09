class Node:
    def __init__(self, key, right=None, left=None, parent=None):
        self.key = key
        self.right = right
        self.left = left
        self.parent = parent

class Tree:
    def __init__(self, root=None):
        self.root = root

def check_odpovidac(tree):
    if tree.root == None:
        return True
    return check_odpovidac_node(tree.root) == tree.root.key


def check_odpovidac_node(node):
    if node == None:
        return 0
    left = check_odpovidac_node(node.left)
    right = check_odpovidac_node(node.right)

    height = 1 + left + right

    if height != node.key:
        return False

    return height

t = Tree()
t.root = Node(7)
t.root.left = Node(5)
t.root.right = Node(1)
t.root.left.left = Node(2)
t.root.left.right = Node(2)
t.root.left.left.left = Node(1)
t.root.left.right.left = Node(1)

tr = Tree(Node(1))

print(check_odpovidac(tr))

