test_cases = [
    ([(10, 5, 2), (15, 4, 3), (30, 7, 5)], 10, 10),
    ([(20, 6, 4), (15, 3, 3), (25, 5, 5), (10, 2, 2), (12, 4, 3)], 12, 10),
    ([(15, 5, 3), (12, 4, 2), (30, 7, 5), (25, 6, 4), (20, 3, 3)], 15, 12),
    ([(10, 4, 2), (20, 5, 3), (15, 3, 2), (25, 6, 4), (18, 4, 3)], 13, 11)
]
for idx, (items, time_limit, weight_limit) in enumerate(test_cases, 1):
    x = []
    for i in range(time_limit + 1):
        row = []
        for j in range(weight_limit + 1):
            row.append(0)
        x.append(row)
    for value, time, weight in items:
        for i2 in range(time_limit, time - 1, -1):
            for i3 in range(weight_limit, weight - 1, -1):
                if x[i2 - time][i3 - weight] + value > x[i2][i3]:
                    x[i2][i3] = x[i2 - time][i3 - weight] + value
    mx_value = 0
    for row in x:
        for value in row:
            if value > mx_value:
                mx_value = value
    mx_value = mx_value
    print(mx_value)