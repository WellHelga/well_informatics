def find_quirky_numbers(x, y, res):
    if x > 10 ** y or x * x >= 10 ** (2 * y):
        return
    N = x * x
    N_str = str(N).zfill(2 * y)
    L = int(N_str[:y])
    R = int(N_str[y:])
    if L + R == x:
        res.append(N_str)
    find_quirky_numbers(x + 1, y, res)
x = int(input())
y = x // 2
res = []
find_quirky_numbers(0, y, res)
print(res)
