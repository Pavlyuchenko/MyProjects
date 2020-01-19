class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head == None:
            new_node = Node(data)

            self.head = new_node
            new_node.prev = None
        else:
            curr = self.head

            while curr.next != None:
                curr = curr.next

            new_node = Node(data)
            new_node.prev = curr
            curr.next = new_node

    def prepend(self, data):
        if self.head == None:
            self.append(data)
        else:
            new_node = Node(data)

            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node
    
    def insert(self, data, index):
        if len(self) == index:
            self.append(data)
            return
        elif index == 0:
            self.prepend(data)
            return
        elif index > len(self):
            return print("You can insert new Node here, because there is not that much Nodes in this Doubly Linked List.\nNo action was done.")

        curr = self.head

        while curr and index > 0:
            curr = curr.next
            index -= 1 

        prev = curr.prev

        new_node = Node(data)

        prev.next = new_node
        curr.prev = new_node

        new_node.prev = prev
        new_node.next = curr

    def print_llist(self):
        curr = self.head
        print("None", "<-", curr.data, end="")
        curr = curr.next
        while curr:
            print(" <->", curr.data, end="")
            curr = curr.next

        print(" -> None")

    def delete(self, index):
        curr = self.head
        if index == 0:
            nxt = curr.next

            nxt.prev = None
            self.head = nxt
            
            curr.next = None
            curr.data = None
            curr = None
            return
        elif len(self) == index+1:
            while curr and index > 0:
                curr = curr.next
                index -= 1

            prev = curr.prev
    
            prev.next = None

            curr.next = None
            curr.data = None
            curr = None
            return
        elif len(self) < index+1:
            return print("There is no that much Nodes in this Doubly Linked List.\nNo action was done.")
            
        while curr and index > 0:
            curr = curr.next
            index -= 1

        prev = curr.prev
        nxt = curr.next

        prev.next = nxt
        nxt.prev = prev

        curr.next = None
        curr.data = None
        curr = None

    def __len__(self):
        curr = self.head
        counter = 0

        while curr:
            counter += 1
            curr = curr.next

        return counter

    def __reversed__(self):
        curr = self.head

        while curr:
            if not curr.next:
                self.head = curr
            curr.prev, curr.next, curr = curr.next, curr.prev, curr.next


    def remove_duplicates(self):
        curr = self.head
        already_used_data = []

        while curr:
            if curr.data in already_used_data:
                if curr.next == None:
                    curr.prev.next = None

                    curr = curr.next
                else:
                    curr.prev.next, curr.next.prev = curr.next, curr.prev

                    curr = curr.next
            else:
                already_used_data.append(curr.data)
                curr = curr.next

    def pairs_with_sum(self, sum):
        pairs = list()
        p = self.head
        q = None
        while p:
            q = p.next
            while q:
                if p.data + q.data == sum:
                    pairs.append(str(p.data) + " + " + str(q.data) + " = " + str(sum))
                q = q.next
            p = p.next
        return pairs


if __name__ == "__main__":
    dllist = DoublyLinkedList()
    dllist.append(1)
    dllist.append(2)
    dllist.append(3)
    dllist.append(4)
    dllist.append(5)
    dllist.append(6)
    dllist.append(4)
    dllist.append(8)


    dllist.print_llist()

    print(dllist.pairs_with_sum(8))

    dllist.print_llist()