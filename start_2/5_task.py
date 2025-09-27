def x(n, k):
    c = 0
    p = k
    while n >= p:
        c += n // p
        p *= k
    return c
n = int(input())
k = int(input())
res = x(n, k)
print(res)
