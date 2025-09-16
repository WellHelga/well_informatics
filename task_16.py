n = int(input())
number = input().split()
b = [0] * (n + 1)
for g in range(0, n + 1):
    s = int(number[g])
    b[s - 1] = g + 1
print(number)
print(b)