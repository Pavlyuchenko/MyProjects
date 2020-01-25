from Data_Struct import Stack

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    
    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, t_type):
        if t_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif t_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif t_type == "postorder":
            return self.postorder_print(tree.root, "")
        elif t_type == "levelorder":
            return self.reverse_level_order_print(tree.root)

    def preorder_print(self, start, traversal):
        if start:
            traversal += str(start.value) + " -> "
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += str(start.value) + " -> "
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += str(start.value) + " -> "
        return traversal

    def level_order_print(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)

        traversal = ""

        while len(queue) > 0:
            node = queue.dequeue()

            traversal += str(node.value) + " -> "

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    def reverse_level_order_print(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)

        s = Stack()
        s.push(str(start.value))

        while len(queue) > 0:
            curr = queue.dequeue()

            if curr.right:
                queue.enqueue(curr.right)
                s.push(str(curr.right.value))
            if curr.left:
                queue.enqueue(curr.left)
                s.push(str(curr.left.value))

        s.print_stack()

    def height(self, node):
        if node is None:
            return -1

        left = self.height(node.left)
        right = self.height(node.right)

        return 1+max(left, right)


                
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.left.left.left = Node(8)
tree.root.left.left.right = Node(9)

print(tree.print_tree("levelorder"))
print(tree.height(tree.root))
