a = int(input())
if a == 0:
    print(0)
else:
    res = ""
    while a > 0:
        b = a % 10
        res = str(b * b) + res
        a = a // 10
    print(int(res))