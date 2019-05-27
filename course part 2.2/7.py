# Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
# Найти сумму элементов всей матрицы.
# Определить, какую долю в этой сумме составляет сумма элементов каждой строки.
# Результат оформить в виде матрицы из N строк и M+1 столбцов.

import numpy as np
import random

N = random.randint(2, 5)
M = random.randint(2, 5)
print(N, M)
A = np.random.randint(0, 100, (N, M))
print(str(A) + "\n")

sm = np.sum(A)

m = []
for i in range(N):
    m.append(np.sum(A[i, :]))
for i in range(N):
    m[i] = round(m[i] / sm, 2)
m = np.array(m)
A = np.hstack((A, m.reshape(-1, 1)))
print(A)
