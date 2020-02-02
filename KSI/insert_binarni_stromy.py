class Node:
    def __init__(self, key, right=None, left=None, parent=None):
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
        return None
    if node.key == value:
        return node
    else:
        if node.left or node.right:
            if value > node.key:
                return find_node(node.right, value)
            else:
                return find_node(node.left, value)
        return None


def insert(tree, value):
    if not tree.root:
        tree.root = Node(value)
        return

    node = tree.root

    while node:
        parent = node
        if value > node.key:
            node = node.right
        else:
            node = node.left

    if value > parent.key:
       parent.right = Node(value)
    else:
        parent.left = Node(value)


def print_tree(node):
    try:
        print(node.key)
        print_tree(node.left)
        print_tree(node.right)
    except:
        pass


tree = Tree()

insert(tree, 4)
insert(tree, 6)
insert(tree, 1)
insert(tree, 3)
insert(tree, 2)
insert(tree, 5)
print_tree(tree.root)

