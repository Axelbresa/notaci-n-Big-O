# O(log n) - Logarítmica
def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print("logaritmica: ", binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))
