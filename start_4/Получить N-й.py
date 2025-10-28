class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(head, index):
    if index < 0:
        raise ValueError("Invalid index or empty list")
    if head is None:
        raise ValueError("Invalid index or empty list")
    x = head
    index_x = 0
    while x is not None:
        if index_x == index:
            return x
        x = x.next
        index_x += 1
    raise ValueError("Index out of range")

list1 = Node(1, Node(2, Node(3)))
result1 = get_nth(list1, 0)
print(result1.data)
list2 = Node(1, Node(2, Node(3, None)))
result2 = get_nth(list2, 2)
print(result2.data)
try:
    get_nth(list2, 5)
except ValueError as e:
    print(e)
try:
    get_nth(None, 0)
except ValueError as e:
    print(e)