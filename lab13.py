import numpy as np
import func

var = 0
while var not in [1, 2]:
    var = int(input("Выберете метод 1 - Якоби, 2 - Зейделя: "))
E = -1
while E < 0:
    E = float(input("Введите погрешность: "))
# A = np.array([[3.1, 0.8, 1.9],[1.9, 3.1, 1.1],[0.5, 3.8, 4.8]])
A = np.array([[10, 1, 1], [2, 10, 1], [2, 2, 10]])
diag = func.diagonal(A)
print("Диагональное преобладание: ", diag)
print()

# b = np.array([0.2, 2.1, 5.6])
b = np.array([12, 13, 14])

print("Система:")
for i in range(A.shape[0]):
    row = ["{} * x{}".format(A[i, j], j + 1) for j in range(A.shape[1])]
    print(" + ".join(row), "=", b[i])
print()
if var == 1:
    func.Jacobi(A, b, E)
if var == 2:
    func.Seidel(A, b, E)
