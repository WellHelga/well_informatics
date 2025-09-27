def number(k1):
    k2 = k1 + 1
    n = 1
    while True:
        x = n * k1
        y = n * k2
        if sorted(str(x)) == sorted(str(y)):
            return n
        n += 1
k1 = int(input())
res = number(k1)
print(res)