# Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Определить, сколько отрицательных элементов
# содержится в каждом столбце и в каждой строке матрицы. Результат
# оформить в виде матрицы из N + 1 строк и M + 1 столбцов.

import numpy as np
import random

N = random.randint(2, 5)
M = random.randint(2, 5)
print(N, M)
A = np.random.randint(-50, 50, (N, M))
print(str(A) + "\n")

M_n = (A < 0).sum(axis=0)
N_n = (A < 0).sum(axis=1)

N_n = np.append(N_n, None)

A = np.vstack((A, M_n))
A = np.hstack((A, N_n.reshape(-1, 1)))
print(A)
