def max_chesspieces(x, m, n):
    if x == "r":
        if m < n:
            return m
        else:
            return n
    elif x == "k":
        return (n * m + 1) // 2
    elif x == "Q":
        if m < n:
            return m
        else:
            return n
    elif x == "K":
        a = (n + 1) // 2
        b = (m + 1) // 2
        return a * b

quantity = int(input())
for i in range(quantity):
    x_m_n = input().split()
    x = x_m_n[0]
    m = int(x_m_n[1])
    n = int(x_m_n[2])
    print(max_chesspieces(x, m, n))

