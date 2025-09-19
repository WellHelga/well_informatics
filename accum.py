def accum(x):
    y1 = []
    for i, j in enumerate(x):
        y2 = j.upper() + j.lower() * i
        y1.append(y2)
    return '-'.join(y1)
z = input()
res = accum(z)
print(res)