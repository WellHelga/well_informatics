g = float(input())
v1 = float(input())
v2 = float(input())
if v1 >= v2:
    print("will not be able to overtake")
else:
    x = g / (v2 - v1)
    print(x)