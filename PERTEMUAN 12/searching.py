def binarySearch(arr, n):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        print(l,mid, r)
        if arr[mid] == n:
            return mid
        elif arr[mid] < n:
            l = mid + 1
        else:
            r = mid - 1
    return -1

print(binarySearch([1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 20, 21, 31, 49], 49))
