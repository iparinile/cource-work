# Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Добавить к матрице столбец чисел и вставить его
# под номером K.

import numpy as np
import random

N = random.randint(2, 5)
M = random.randint(2, 5)
print("N =", str(N), " - ", "M =", str(M))
A = np.random.randint(-50, 50, (N, M))
print(str(A) + "\n")

K = random.randint(0, M-1)
print("K =", str(K+1))
K_n = np.random.randint(-50, 50, (1, N))
print("Вставляемый столбец -", str(K_n))

A = np.insert(A, K, K_n, axis=1)
print(A)
