def binary_search(arr, key):
    lo = 0
    hi = len(arr)-1

    while lo <= hi:
        mid = lo + (hi-lo) // 2

        if arr[mid] < key:
            lo = mid + 1
        elif arr[mid] > key:
            hi = mid - 1
        else:
            return mid
    return -1


def binary_search_(arr, key, lo, hi):
    if lo > hi:
        return -1

    mid = lo + (hi - lo) // 2

    if arr[mid] < key:
        lo = mid + 1
    elif arr[mid] > key:
        hi = mid - 1
    else:
        return mid

    return binary_search_(arr, key, lo, hi)


arr = [1, 2]
assert 0 == binary_search(arr, 1)
assert 1 == binary_search_(arr, 2, 0, len(arr)-1)

