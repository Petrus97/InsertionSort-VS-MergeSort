def mergesort(A, p, r):
    if(p < r):
        q = int((p + r)/2)
        mergesort(A, p, q)
        mergesort(A, q+1, r)
        merge(A, p, q, r)
    return A


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0]*(n1+1)
    R = [0]*(n2+1)
    i = 1
    j = 1
    while i <= n1:
        L[i-1] = A[p+i-1]
        i = i + 1
    while j <= n2:
        R[j-1] = A[q+j]
        j = j + 1
    L[n1] = float("inf")  # tips from StackOverflow
    R[n2] = float("inf")
    i = 0
    j = 0
    for k in range(p, r + 1):
        if(L[i] < R[j]):
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
    return A
