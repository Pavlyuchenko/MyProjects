class Node:
    def __init__(self, key, right=None, left=None, parent=None):
        self.key   = key
        self.right = right
        self.left = left
        self.parent = parent


class Tree:
    def __init__(self, root=None):
        self.root = root


def insert(tree, key):
    node = tree.root
    parent = None
    while node is not None:
        parent = node
        if node.key <= key:
            node = node.right
        else:
            node = node.left
    node = Node(key)
    node.parent = parent
    if parent is None:
        tree.root = node
    else:
        if parent.key <= key:
            parent.right = node
        else:
            parent.left = node


def build_culm(tree):
    for i in range(6):
        insert(tree, i)

T = Tree()

build_culm(T)

def print_tree(node):
    try:
        print(node.key)
        print_tree(node.left)
        print_tree(node.right)
    except:
        pass

print_tree(T.root)
