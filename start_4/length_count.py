class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def length(head):
    count = 0
    x = head
    while x is not None:
        count += 1
        x = x.next
    return count

def count(head, value):
    value_count = 0
    x = head
    while x is not None:
        if x.data == value:
            value_count += 1
        x = x.next
    return value_count

list1 = Node(1, Node(2, Node(3)))
result_length = length(list1)
print(result_length)

result_count = count(list1, 1)
print(result_count)

list2 = Node(1, Node(1, Node(1, Node(2, Node(2, Node(2, Node(2, Node(3, Node(3)))))))))
result_count_2 = count(list2, 2)
print(result_count_2)