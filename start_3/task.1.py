x = input().split()
sizes = []
for i in x:
    n = int(i)
    if n > 0:
        sizes.append(n)
print(f"{"n":>6} {"O(1)":>8} {"O(log n)":>10} {"O(sqrt(n))":>12} {"O(n)":>6} {"O(n log n)":>12} {"O(n**2)":>10} {"O(n**3)":>10} {"O(2**n)":>10} {"O(n!)":>10}")
print("-" * 110)
for n in sizes:
    o_1 = 1
    o_log_n = 0
    y = n
    while y > 1:
        y //= 2
        o_log_n += 1
    if (1 < o_log_n) != n:
        o_log_n += 0.5
    o_log_n = round(o_log_n, 2)
    o_sqrt_n = round(n ** 0.5, 2)
    o_n = n
    o_n_log_n = round(n * o_log_n, 2)
    o_n2 = n ** 2
    o_n3 = n ** 3
    o_2n = 2 ** n
    o_n_fact = 1
    for j in range(2, n + 1):
        o_n_fact *= j
    print(f"{n:>6} {o_1:>8} {o_log_n:>10} {o_sqrt_n:>12} {o_n:>6} {o_n_log_n:>12} {o_n2:>10} {o_n3:>10} {o_2n:>10} {o_n_fact:>10}")