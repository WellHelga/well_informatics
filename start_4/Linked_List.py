class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        node2 = Node(data)
        if self.is_empty():
            self.head = node2
        else:
            x = self.head
            while x.next:
                x = x.next
            x.next = node2

    def prepend(self, data):
        node2 = Node(data)
        node2.next = self.head
        self.head = node2

    def delete(self, data):
        if self.is_empty():
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        x = self.head
        while x.next and x.next.data != data:
            x = x.next
        if x.next:
            x.next = x.next.next

    def display(self):
        if self.is_empty():
            print("List is empty")
            return
        x = self.head
        y = []
        while x:
            y.append(str(x.data))
            x = x.next
        print("-".join(y))

my_linked_list = LinkedList()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.prepend(0)
my_linked_list.display()
my_linked_list.delete(2)
my_linked_list.display()