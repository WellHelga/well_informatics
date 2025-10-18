# a = int(input())
# b = int(input())
# c = int(input())

def kb_b(kb):
    return kb * 1024
def b_kb(b):
    return b / 1024
print("1. kb in b")
print("2. b in kb")

x = input()
y = int(input())

if x == "1":
    res = kb_b(y)
    print(y, "kb =", res, "b")
elif x == "2":
    res = b_kb(y)
    print(y, "b =", res, "kb")


