x = list(map(int, input().split()))
y = list(map(int, input().split()))
res = []
for i in x:
    if i not in y:
        res.append(i)
print(res)