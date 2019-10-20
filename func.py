import numpy as np
def diagonal(A):
    diag = True
    for i in range(0,len(A)):
        sum1 = sum(A[i])
        result = sum1 - A[i][i]
        if result > A[i][i]:
            diag = False
    return diag