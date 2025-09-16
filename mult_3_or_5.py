x = int(input())
if x <= 0:
    res = 0
else:
    res = 0
    for i in range(1, x):
        if i % 3 == 0 or i % 5 == 0:
            res += i
print(res)