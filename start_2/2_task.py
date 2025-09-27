numbers = {
    "bk": 0, "br": 1, "rd": 2, "or": 3, "yl": 4, "gr": 5,
    "bl": 6, "vi": 7, "gy": 8, "wh": 9
}
multiplier = {
    "bk": 1, "br": 10, "rd": 100, "or": 1000, "yl": 10000, "gr": 10000,
    "bl": 100000, "vi": 1000000, "gy": 100000000, "wh": 1000000000
}
deviation = {
    "br": 1, "rd": 2, "gr": 0.5, "bl": 0.25, "vi": 0.1, "gy": 0.05,
    "au": 5, "ag": 10
}
x = input().split()
# x1, x2, x3, x4 = x
if len(x) != 4:
    print("Fewer than four colours provided in bands")
else:
    x1, x2, x3, x4 = x
    if x1 not in numbers or x2 not in numbers or x3 not in multiplier or x4 not in deviation:
        print("Unidentified or invalid band colour in bands")
    else:
        res = (numbers[x1] * 10 + numbers[x2]) * multiplier[x3]
        print(res)
        print(deviation[x4])