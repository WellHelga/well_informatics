def max_sequence(x):
    if not x:
        return 0
    ms = 0
    s = 0
    for i in x:
        s = max(0, s + i)
        ms = max(ms, s)
    return ms
x = list(map(int, input().split()))
res = max_sequence(x)
print(res)
