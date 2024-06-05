# O(2^n) - Exponencial
def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs(X, Y, m-1, n-1)
    else:
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))

x = "AGGTAB"
y = "GXTXAYB"
print("Exponencial: ", lcs(x, y, len(x), len(y)) ) 
