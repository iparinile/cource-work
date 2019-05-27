# Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Все элементы имеют целый тип. Дано целое число H.
# Определить, какие столбцы имеют хотя бы одно такое число, а какие не имеют.

import numpy as np
import random

N = random.randint(3, 5)
M = random.randint(3, 5)
print(N, M)
A = np.random.randint(1, 5, (N, M))
print(str(A) + "\n")

H = random.randint(1, 4)
print("H = " + str(H))

im = []
nim = []
for i in range(M):
    if H in A[:, i]:
        im.append(i+1)
    else:
        nim.append(i+1)

print("Столбцы, которые имеют хотя бы одно число H - " + str(im))
print("Столбцы, которые не имеют это число - " + str(nim))

