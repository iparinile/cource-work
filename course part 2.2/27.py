# Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
# Все элементы имеют целый тип. Дано целое число H. Определить, какие строки имеют хотя бы одно
# такое число, а какие не имеют.

import numpy as np
import random

N = random.randint(2, 5)
M = random.randint(2, 5)
print("N =", str(N), " - ", "M =", str(M))
A = np.random.randint(1, 4, (N, M))
print(str(A) + "\n")

im = []
neim = []
H = random.randint(1, 4)
print("H =", str(H))
for i in range(N):
    if H in A[i, :]:
        im.append(i+1)
    else:
        neim.append(i+1)
print("Строки,которые имеют хотя бы одно число H -", str(im))
print("Строки, которые не имеют число H -", str(neim))
