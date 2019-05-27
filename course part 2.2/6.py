# Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
# Найти сумму элементов всей матрицы.
# Определить, какую долю в этой сумме составляет сумма элементов каждого столбца.
# Результат оформить в виде матрицы из N + 1 строк и M столбцов.

import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)
print(N, M)
A = np.random.randint(0, 100, (N, M))
print(str(A) + "\n")

sm = np.sum(A)

m = []
for i in range(M):
    m.append(np.sum(A[:, i]))
for i in range(M):
    m[i] = round(m[i] / sm, 2)
A = np.vstack((A, m))
print(A)
