# Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Добавить к матрице строку и вставить ее под
# номером L.

import numpy as np
import random

N = random.randint(2, 5)
M = random.randint(2, 5)
print(N, M)
A = np.random.randint(-50, 50, (N, M))
print(str(A) + "\n")

L = random.randint(0, N-1)
print("L =", str(L+1))
L_n = np.random.randint(-50, 50, (1, M))
print("Вставляемая строка -", str(L_n))

A = np.insert(A, L, L_n, axis=0)
print(A)
