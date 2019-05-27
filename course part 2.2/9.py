# Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
# Определить, сколько нулевых элементов
# содержится в верхних L строках матрицы и в левых К столбцах матрицы.

import numpy as np
import random

N = random.randint(2, 10)
M = random.randint(2, 10)
print(N, M)
A = np.random.randint(-2, 2, (N, M))
print(str(A) + "\n")

L = random.randint(1, N)
K = random.randint(1, M)
print("L = " + str(L) + "    " + "K = " + str(K))
L_n = 0
K_n = 0

for i in A[:L].flat:
    if i == 0:
        L_n += 1

for i in A[:, : K].flat:
    if i == 0:
        K_n += 1

print("Количество нулевых элементов в верхних " + str(L) + " строках матрицы - " + str(L_n))
print("Количество нулевых элементов в левых " + str(K) + " столбцах матрицы - " + str(K_n))
