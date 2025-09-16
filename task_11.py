m = input().split()
for i in range(len(m)):
    m[i] = int(m[i])
min_m = min(m)
min_i = m.index(min_m)
print(min_i)