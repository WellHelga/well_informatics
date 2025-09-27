x = input()
if not x:
    print("Percentages of bases G and C:", 0)
    print("None")
else:
    z = x.count("G") + x.count("C")
    res = 100 * (z / len(x))
    print("Percentages of bases G and C:", res)
    a = x.replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c")
    b = a.upper()
    if x == b[::-1]:
        print("Palindrome")
    else:
        print("It is not a palindrome")