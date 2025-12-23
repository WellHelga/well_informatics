class HuffmanNode:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right


class HuffmanTree:
    def __init__(self, text):
        self.text = text
        self.root = None
        self.codes = {}

    def build_tree(self):
        freq = {}
        for char in self.text:
            freq[char] = freq.get(char, 0) + 1
        if not freq:
            return
        s = []
        for char, i in freq.items():
            s.append(HuffmanNode(char, i))

        while len(s) > 1:
            s.sort(key=lambda node: node.freq)
            left = s.pop(0)
            right = s.pop(0)
            res = HuffmanNode(None, left.freq + right.freq, left, right)
            s.append(res)
        self.root = s[0]
        self._generate_codes(self.root, "")

    def _generate_codes(self, node, current_code):
        if node is None:
            return
        if node.char is not None:
            if current_code == "":
                self.codes[node.char] = "0"
            else:
                self.codes[node.char] = current_code
            return
        self._generate_codes(node.left, current_code + "0")
        self._generate_codes(node.right, current_code + "1")


    def encode(self, text):
        if self.root is None:
            self.build_tree()
        res = ""
        for char in text:
            res += self.codes.get(char, "")
        return res

    def decode(self, encoded_text):
        if self.root is None:
            return ""
        decoded = []
        current = self.root
        for bit in encoded_text:
            if bit == '0':
                current = current.left
            else:
                current = current.right
            if current.char is not None:
                decoded.append(current.char)
                current = self.root
        return ''.join(decoded)

result = HuffmanTree("hello, world")
result.build_tree()
print(result.codes)
code = result.encode("hello, world")
print(code)
print(result.decode(code))