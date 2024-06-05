# O(n) - Lineal
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

print("lineal: ", linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))