# Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Добавить к элементам каждого столбца такой
# новый элемент, чтобы сумма положительных элементов стала бы равна
# модулю суммы отрицательных элементов. Результат оформить в виде
# матрицы из N + 1 строк и M столбцов.

import numpy as np
import random

N = random.randint(2, 5)
M = random.randint(2, 5)
print("N =", str(N), " - ", "M =", str(M))
A = np.random.randint(-50, 50, (N, M))
print(str(A) + "\n")

M_n = np.sum(A, axis=0) * (-1)
A = np.vstack((A, M_n))
print(A)
