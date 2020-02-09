class Node:
    def __init__(self, key, right=None, left=None, parent=None):
        self.key = key
        self.right = right
        self.left = left
        self.parent = parent

class Tree:
    def __init__(self, root=None):
        self.root = root


def check_dluhoruk(tree):
    return check_dluhoruk_node(tree.root)

def check_dluhoruk_node(node):
    if node.left and node.right:
        left = check_dluhoruk_node(node.left)
        right = check_dluhoruk_node(node.right)

        if 1 + left[1] + right[1] > max(left[0], right[0]):
            longest = 1 + left[1] + right[1]
        else:
            longest = max(left[0], right[0])
        optional = 1 + max(left[1], right[1])
        current = left[1] + right[1]

        return [longest, optional, current]

    elif node.left:
        left = check_dluhoruk_node(node.left)

        if 1 + left[1] > left[0]:
            longest = 1 + left[1]
        else:
            longest = left[0]
        optional = longest

        return [longest, optional]
    elif node.right:
        right = check_dluhoruk_node(node.right)

        if 1 + right[1] > right[0]:
            longest = 1 + right[1]
        else:
            longest = right[0]
        optional = longest

        return [longest, optional]
    return [1, 1]

'''def check_dluhoruk(tree):
    res = check_dluhoruk_node(tree.root, 0, 0)
    print(res)
    return res[0] <= res[1]


def check_dluhoruk_node(node, curr_max, longest_road):
    if not node:
        return [1, 1]

    cdn_left = check_dluhoruk_node(node.left, curr_max, longest_road)
    cdn_right = check_dluhoruk_node(node.right, curr_max, longest_road)

    curr_max = cdn_left[0] + cdn_right[0]
    longest_road = max(cdn_left[1], cdn_right[1])

    return [curr_max, longest_road]'''


t = Tree()
t.root = Node(0)
t.root.left = Node(1)
t.root.right = Node(8)
t.root.left.left = Node(2)
t.root.left.right = Node(5)
t.root.left.left.left = Node(3)
t.root.left.right.right = Node(4)

t1 = Tree()
t1.root = Node(0)
t1.root.left = Node(1)
t1.root.right = Node(6)
t1.root.right.right = Node(7)
t1.root.left.left = Node(2)
t1.root.left.right = Node(5)
t1.root.left.left.left = Node(3)
t1.root.left.left.right = Node(4)

print(check_dluhoruk(t1))
