class TreeNode:
    def __init__(self, data):
        self.data = data
        self.lt = None
        self.rt = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.lt is None:
                node.lt = TreeNode(data)
            else:
                self._insert_recursive(node.lt, data)
        elif data > node.data:
            if node.rt is None:
                node.rt = TreeNode(data)
            else:
                self._insert_recursive(node.rt, data)

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search_recursive(node.lt, data)
        else:
            return self._search_recursive(node.rt, data)

    def in_order_traversal(self):
        res = []
        self._in_order_recursive(self.root, res)
        return res

    def _in_order_recursive(self, node, res):
        if node:
            self._in_order_recursive(node.lt, res)
            res.append(node.data)
            self._in_order_recursive(node.rt, res)

    def pre_order_traversal(self):
        res = []
        self._pre_order_recursive(self.root, res)
        return res

    def _pre_order_recursive(self, node, res):
        if node:
            res.append(node.data)
            self._pre_order_recursive(node.lt, res)
            self._pre_order_recursive(node.rt, res)

    def post_order_traversal(self):
        res = []
        self._post_order_recursive(self.root, res)
        return res

    def _post_order_recursive(self, node, res):
        if node:
            self._post_order_recursive(node.lt, res)
            self._post_order_recursive(node.rt, res)
            res.append(node.data)

tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
print(tree.search(5))
print(tree.search(20))
print(tree.in_order_traversal())
print(tree.pre_order_traversal())
print(tree.post_order_traversal())