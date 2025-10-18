def binary_search(arr, target, lt = 0, rt = None):
    if rt is None:
        rt = len(arr) - 1
    if lt > rt:
        return -1
    mid = (lt + rt) // 2
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, lt, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, rt)
n = list(map(int, input().split()))
x = int(input())
res = binary_search(n,x)
print(res)
