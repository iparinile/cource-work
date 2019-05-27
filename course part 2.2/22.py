# Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Исходная матрица состоит из нулей и единиц.
# Добавить к матрице еще один столбец, каждый элемент которого делает
# количество единиц в каждой строке чётным.

import numpy as np
import random

N = random.randint(2, 5)
M = random.randint(2, 5)
print("N =", str(N), ",", "M =", str(M))
A = np.random.randint(0, 2, (N, M))
print(str(A) + "\n")

New_s = []
for i in range(N):
    if A[i, :].sum() % 2 == 0:
        New_s.append(0)
    else:
        New_s.append(1)
A = np.insert(A, M, New_s, axis=1)
print(A)
