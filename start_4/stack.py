class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError()
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError()
        return self.items[-1]

    def size(self):
        return len(self.items)

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print("Stack:", my_stack.items)
popped_item = my_stack.pop()
print("Popped item:", popped_item)
top_item = my_stack.peek()
print("Top item:", top_item)
print("Is stack empty?", my_stack.is_empty())
print("Stack size:", my_stack.size())