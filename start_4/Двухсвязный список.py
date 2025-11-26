class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newnode
            newnode.prev = current

    def prepend(self, data):
        newnode = Node(data)
        if self.head:
            newnode.next = self.head
            self.head.prev = newnode
        self.head = newnode

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end = "<->")
            current = current.next
        print("None")

    def display_reverse(self):
        current = self.head
        if not current:
            return
        while current.next:
            current = current.next
        while current:
            current = current.prev

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.display()

dll.prepend(0)
dll.display()

dll.delete(2)
dll.display()

dll.display_reverse()