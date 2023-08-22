import numpy as np


def create_matrix(arr):
    column = len(arr[0])
    if len(arr) > 1:
        for item in arr:
            if len(item) != column:
                return False

    return np.array(arr)


def ident_determinant(A):
    n = len(A)

    if n == 2:
        return A[0][0]*A[1][1]-A[0][1]*A[1][0]

    det = 0

    for j in range(n):
        M = np.delete(np.delete(A, 0, 0), j, 1)
        sign = (-1) ** (j % 2)
        det += sign * A[0, j] * ident_determinant(M)

    return det


A = create_matrix([[1, 2, 0], [4, 5, 4], [1, 2, 6]])


print(ident_determinant(A))
