# Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Перемножить элементы каждого столбца матрицы
# с соответствующими элементами K-го столбца.

import numpy as np
import random

N = random.randint(2, 5)
M = random.randint(2, 5)
print(N, M)
A = np.random.randint(-50, 50, (N, M))
print(str(A) + "\n")

K = random.randint(0, M)
print("K = " + str(K + 1))
K_m = A[:, K].flat

for i in range(M):
    if i != K:
        for k in range(N):
            A[k, i] = A[k, i] * K_m[k]
print(A)
