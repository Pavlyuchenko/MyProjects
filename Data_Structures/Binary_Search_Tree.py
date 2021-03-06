class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, curr):
        if data < curr.data:
            if curr.left is None:
                curr.left = Node(data)
            else:
                self._insert(data, curr.left)
        elif data > curr.data:
            if curr.right is None:
                curr.right = Node(data)
            else:
                self._insert(data, curr.right)
        else:
            print("Value is already in the tree")

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self, data, curr):
        if curr.data == data:
            return True
        else:
            if data < curr.data and curr.left:
                return self._find(data, curr.left)
            elif data > curr.data and curr.right:
                return self._find(data, curr.right)

    def inorder_print_tree(self):
        if self.root:
            self._inorder_print_tree(self.root)

    def _inorder_print_tree(self, curr):
        if curr:
            self._inorder_print_tree(curr.left)
            print(str(curr.data) + " < ", end="")
            self._inorder_print_tree(curr.right)

bst = BinarySearchTree()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)  
bst.insert(9)  
bst.insert(11)  

print(bst.find(2))
print(bst.inorder_print_tree())
    