test_cases = [
    ([(2, 10), (3, 15), (5, 30)], 5),
    ([(2, 10), (3, 15), (5, 30), (7, 20), (1, 5), (4, 10)], 10),
    ([(2, 20), (3, 15), (5, 30), (1, 25), (4, 10)], 7),
    ([(2, 5), (3, 8), (5, 15), (1, 3), (4, 10)], 7),
    ([(6, 10), (8, 15), (12, 30)], 5)
]
for idx, (items, limit) in enumerate(test_cases, 1):
    x = [0] * (limit + 1)
    for weight, value in items:
        for i in range(limit, weight - 1, -1):
            if x[i - weight] + value > x[i]:
                x[i] = x[i - weight] + value
    print(idx, x[limit])