import numpy as np
import func
ITERATION_LIMIT = 1000

A = np.array([[3.1, 0.8, 1.9],[1.9, 3.1, 1.1],[0.5, 3.8, 4.8]])
diag = func.diagonal(A)
print("Диагональное преобладание: ", diag)

b = np.array([0.2, 2.1, 5.6])

print("System:")
for i in range(A.shape[0]):
    row = ["{}*x{}".format(A[i, j], j + 1) for j in range(A.shape[1])]
    print(" + ".join(row), "=", b[i])
print()

x = np.zeros_like(b)
for it_count in range(ITERATION_LIMIT):
    print("Current solution:", x)
    x_new = np.zeros_like(x)

    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x[:i])
        s2 = np.dot(A[i, i + 1:], x[i + 1:])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]
    exit = False
    for n in range(A.shape[0]):
        if abs(x_new[n] - x[n])<0.001:
            exit = True
    #if np.allclose(x, x_new, atol=0.001, rtol=0.0):
    if exit == True:
        break
    x = x_new

print("Solution:")
print(x)
error = np.dot(A, x) - b
print("Error:")
print(error)