# Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Исключить из матрицы столбец с номером K.
# Сомкнуть столбцы матрицы.

import numpy as np
import random

N = random.randint(2, 5)
M = random.randint(2, 5)
print("N =", str(N), " - ", "M =", str(M))
A = np.random.randint(1, 4, (N, M))
print(str(A) + "\n")

K = random.randint(1, M-1)
print("K =", str(K+1))

A = np.delete(A, K, axis=1)
print(A)
