# Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Разделить элементы каждой строки на элемент
# этой строки с наибольшим значением.

import numpy as np
import random

N = random.randint(2, 5)
M = random.randint(2, 5)
print(N, M)
A = np.random.randint(-50, 50, (N,M))
A = np.array(A, float)

print(str(A) + "\n")

for i in range(N):
    mx = np.max(A[i, :])
    for k in range(M):
        if A[i, k] != mx:
            A[i, k] = round(A[i, k] / mx, 2)
print(A)
