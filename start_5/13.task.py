def hamming(n):
    hamming = [1]
    i2 = i3 = i5 = 0
    for _ in range(1, n):
        x2 = hamming[i2] * 2
        x3 = hamming[i3] * 3
        x5 = hamming[i5] * 5
        x_hamming = min(x2, x3, x5)
        hamming.append(x_hamming)
        if x_hamming == x2:
            i2 += 1
        if x_hamming == x3:
            i3 += 1
        if x_hamming == x5:
            i5 += 1
    return hamming[-1]
print(hamming(1))
print(hamming(2))
print(hamming(3))
print(hamming(4))
print(hamming(5))
print(hamming(20))
