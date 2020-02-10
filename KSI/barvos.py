class Node:
    def __init__(self, key, right=None, left=None, parent=None):
        self.key = key
        self.right = right
        self.left = left
        self.parent = parent

class Tree:
    def __init__(self, root=None):
        self.root = root

'''
def check_barvos(tree, colours, length):
    node_count = check_barvos_node(tree.root)
    return node_count

def check_barvos_node(node):
    if not node:
        return 0

    return 1 + check_barvos_node(node.left) + check_barvos_node(node.right)
'''


def node_barvos(node, length):
    if node is not None:
        l = node_barvos(node.left, length)
        r = node_barvos(node.right, length)
        done = l[0]+r[0]
        unused = max(l[1],r[1]) + 1
        if l[1]+r[1]+1 >= length:
            unused = 0
            done += 1
        return (done, unused)
    return (0,0)

def check_barvos(tree, colours, length):
    if tree is not None:
        return node_barvos(tree.root, length)[0] >= colours
    return False

t = Tree()
t.root = Node(0)
t.root.left = Node(1)
t.root.left.left = Node(2)
t.root.left.right = Node(4)
t.root.left.left.left = Node(3)
t.root.right = Node(5)
t.root.right.left = Node(6)
t.root.right.right = Node(7)


t1 = Tree()
t1.root = Node(0)
t1.root.left = Node(1)
t1.root.left.left = Node(2)
t1.root.left.right = Node(4)
t1.root.left.left.left = Node(3)
t1.root.right = Node(5)
t1.root.right.left = Node(6)
t1.root.right.right = Node(9)
t1.root.right.left.left = Node(7)
t1.root.right.left.right = Node(8)

print(check_barvos(t1, 3, 4))
