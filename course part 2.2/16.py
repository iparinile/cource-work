# Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Исключить из матрицы строку с номером L.
# Сомкнуть строки матрицы.

import numpy as np
import random

N = random.randint(2, 5)
M = random.randint(2, 5)
print(N, M)
A = np.random.randint(-50, 50, (N, M))
print(str(A) + "\n")

L = random.randint(0, N-1)
print("L = " + str(L+1))
A = np.delete(A, L, axis=0)

print(A)
