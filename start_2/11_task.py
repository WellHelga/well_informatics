def factorial(n):
    if n < 0:
        return None
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res
n = int(input())
result = factorial(n)
print(result)
