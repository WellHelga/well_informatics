day = int(input())
number = int(input())
print("su mo tu we th fr sa")
x = "   " * (day - 1)
for number in range(1, number + 1):
    x += f"{number:2d} "
    if (day - 1 + number) % 7 == 0:
        print(x)
        x = ""
if x:
    print(x)