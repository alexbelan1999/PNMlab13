import numpy as np
import math


def diagonal(A):
    diag = True
    for i in range(0, len(A)):
        sum1 = sum(A[i])
        result = sum1 - A[i][i]
        if result > A[i][i]:
            diag = False
    return diag


def check(x_new, x, E):
    return math.sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(len(x)))) <= E


def Jacobi(A, b, E):
    maxA = 0
    for i in range(0, A.shape[0]):
        if A[i, i] > maxA:
            maxA = A[i, i]
    x = b / maxA
    it_count = 1
    while (True):
        x_new = b / maxA
        for i in range(0, A.shape[0]):
            # print("A[i, :i]: ", A[i, :i])
            # print("x[:i]: ", x[:i])
            s1 = np.dot(A[i, :i], x[:i])
            # print("s1: ", s1)
            # print("A[i, i + 1:]: ", A[i, i + 1:])
            # print("x[i + 1:]: ", x[i + 1:])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            # print("s2: ", s2)
            # print("x_new",[i]," = " ,b[i]/ A[i, i]," - ",s1/ A[i, i]," - ",s2/ A[i, i])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]

        iter = 0
        for n in range(0, A.shape[0]):
            if abs(x_new[n] - x[n]) <= E:
                iter += 1

        x = x_new
        print("Итерация ", it_count, " решение на данной итерации:", x)
        if iter == 3:
            break
        it_count += 1

    print()
    print("Решение системы: ")
    print(x)

    error = np.dot(A, x) - b
    print()
    print("Погрешность: ")
    print(error)
    pass


def Seidel(A, b, E):
    maxA = 0
    for i in range(0, A.shape[0]):
        if A[i, i] > maxA:
            maxA = A[i, i]
    x = b / maxA
    it_count = 1
    while (True):
        x_new = b / maxA
        B = []
        for i in range(0, A.shape[0]):
            # print("A[i, :i]: ", A[i, :i])
            # print("x_new[:i]: ", x_new[:i])
            s1 = np.dot(A[i, :i], x_new[:i])
            # print("s1: ", s1)
            # print("A[i, i + 1:]: ", A[i, i + 1:])
            # print("x[i + 1:]: ", x[i + 1:])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            # print("s2: ", s2)
            # print("x_new",[i]," = " ,b[i]/ A[i, i]," - ",s1/ A[i, i]," - ",s2/ A[i, i])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
            B.insert(i, [s1 / A[i, i], s2 / A[i, i]])
            B[i].insert(i, 0)

        if np.linalg.norm(B, np.inf) > 1:
            print("Норма больше 1!")
            break

        iter = 0
        for n in range(0, A.shape[0]):
            if abs(x_new[n] - x[n]) <= E:
                iter += 1

        x = x_new
        print("Итерация ", it_count, " решение на данной итерации:", x)
        if iter == 3:
            break
        it_count += 1

    print()
    print("Решение системы: ")
    print(x)

    error = np.dot(A, x) - b
    print()
    print("Погрешность: ")
    print(error)
    pass
