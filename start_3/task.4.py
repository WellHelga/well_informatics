def linear_search(arr, target, x = 0):
    if x >= len(arr):
        return -1
    if arr[x] == target:
        return x
    return linear_search(arr, target, x + 1)
n = list(map(int, input().split()))
y = int(input())
res = linear_search(n, y)
print(res)
