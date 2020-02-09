class Node:
    def __init__(self, key, right=None, left=None, parent=None):
        self.key = key
        self.right = right
        self.left = left
        self.parent = parent

class Tree:
    def __init__(self, root=None):
        self.root = root


def check_vyrovnan(tree):
    return check_vyrovnan_node(tree.root)


def check_vyrovnan_node(node):
    if not node:
        return True

    if not node.left:
        left = 0
    else:
        left = node.left.key
    if not node.right:
        right = 0
    else:
        right = node.right.key

    if abs(left - right) > 1:
        return False
    return True and check_vyrovnan_node(node.left) and check_vyrovnan_node(node.right)


t = Tree()
t.root = Node(3)
t.root.left = Node(2)
t.root.right = Node(1)
t.root.left.left = Node(2)
t.root.left.right = Node(1)
t.root.left.left.left = Node(3)
t.root.left.left.right = Node(4)

tr = Tree(Node(7))
print(check_vyrovnan(tr))
