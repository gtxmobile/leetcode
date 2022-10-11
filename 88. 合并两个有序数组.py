def merge(A, m, B, n):
    i = m - 1
    j = n - 1
    head = m + n - 1
    while i > -1 and j > -1:
        if A[i] > B[j]:
            A[head] = A[i]
            i -= 1
        else:
            A[head] = B[j]
            j -= 1
        head -= 1
        print
        A
    if i < 0:
        A[:head + 1] = B[:j + 1]


B = [1, 2, 3]
A = [4, 5, 6]
A.extend(B)

merge(A, 3, B, len(B))
print
A
