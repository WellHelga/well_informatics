x = 1
y = 2
summ = 0
while y <= 4000000:
    if y % 2 == 0:
        summ += y
    x, y = y, x + y
print(summ)