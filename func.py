import numpy as np
def diagonal(A):
    diag = True
    for i in range(0,len(A)):
        sum1 = sum(A[i])
        result = sum1 - A[i][i]
        if result > A[i][i]:
            diag = False
    return diag

def Jacobi(A,b,E):
    x = np.zeros_like(b)
    it_count = 0
    while (True):
        print("Итерация ", it_count, " решение на данной итерации:", x)
        x_new = np.zeros_like(x)

        for i in range(0,A.shape[0]):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            #print("x_new = " ,b[i]," - ",s1," - ",s2)
            x_new[i] = (b[i] - s1 - s2) / A[i, i]

        exit = False
        for n in range(0, A.shape[0]):
            if abs(x_new[n] - x[n]) <= E:
                exit = True
        if exit == True:
            break
        x = x_new
        it_count += 1

    print()
    print("Решение системы: ")
    print(x)

    error = np.dot(A, x) - b
    print()
    print("Погрешность: ")
    print(error)
    pass
