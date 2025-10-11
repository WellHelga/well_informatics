def snail(x):
    if not x or not x[0]:
        return []
    res = []
    while x:
        res += x.pop(0)
        x = list(zip(*x))[::-1]
    return res
size = int(input())
x = []
for i in range(size):
    y = list(map(int, input().split()))
    x.append(y)
result = snail(x)
print(result)
