def tetration(n, x):
    if n == 0:
        return 1
    if n == 1:
        return x
    return x ** tetration(n - 1,  x)
n = int(input())
x = int(input())
result = tetration(n, x)
print(len(str(result)))
