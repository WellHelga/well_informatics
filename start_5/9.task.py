test_cases = [
    ([(2, 5), (3, 8), (5, 15), (1, 3), (4, 10)], 7, 18),
    ([(6, 10), (8, 15), (12, 30)], 5, 0),
    ([(1, 1), (2, 6), (3, 10), (4, 15), (5, 20)], 7, 26)
]
def memoizac(items, capacity):
    mem = {}
    def f(i, j):
        if i >= len(items) or j <= 0:
            return 0
        if (i, j) in mem:
            return mem[(i, j)]

        weight, value = items[i]
        res = f(i + 1, j)
        if weight <= j:
            res = max(res, value + f(i + 1, j - weight))
        mem[(i, j)] = res
        return res
    return f(0, capacity)
for items, capacity2, expected in test_cases:
    result = memoizac(items, capacity2)
    print(result)

if __name__ == "__main__":
    pass