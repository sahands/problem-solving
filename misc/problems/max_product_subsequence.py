def max_subsequence_product(A):
    a = b = m = A[0]
    for x in A[1:]:
        a, __, b = tuple(sorted([a * x, b * x, x]))
        m = max(b, m)
    return m

print max_subsequence_product([1, -1, 2, 4, -2])
print max_subsequence_product([-5, -2, 2, -30])
print max_subsequence_product([-5, -2, 2, -3, 0, 3, 10, 0, 5, -10, -2])




