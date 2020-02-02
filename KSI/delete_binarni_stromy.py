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


def delete_node(tree, value):
    node = find_node(tree.root, value)
    if node is None:
        return False

    if node.left == None and node.right == None:
        if node.parent == None:
            tree.root = None
        elif node.parent.left == node:
            node.parent.left = None
        else:
            node.parent.right = None

    elif node.right == None:
        if node.parent == None:
            node.root = node.left
        elif node.parent.left == node:
            node.parent.left = node.left
        else:
            node.parent.right = node.left
    elif node.left == None:
        if node.parent == None:
            node.root = node.left
        elif node.parent.left == node:
            node.parent.left = node.right
        else:
            node.parent.right = node.right

    else:
        succ_key = closest_node(node).key
        delete_node(tree, succ_key)
        node.key = succ_key


def closest_node(node):
    node = node.right

    while node.left:
        node = node.left

    return node


def print_tree(node):
    try:
        print(node.key)
        print_tree(node.left)
        print_tree(node.right)
    except:
        pass


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

node8.parent = node15
node5.parent = node8
node2.parent = node5
node11.parent = node8
node10.parent = node11
node12.parent = node11

node20.parent = node15
node18.parent = node20
node17.parent = node18
node23.parent = node31
node31.parent = node20




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

delete_node(T, 12)
delete_node(T, 20)
delete_node(T, 5)
delete_node(T, 15)
delete_node(T, 8)
delete_node(T, 17)
print_tree(T.root)
