# Создать квадратную матрицу A, имеющую N строк и N столбцов со случайными элементами.
# Каждой паре элементов, симметричныхотносительно главной диагонали
# (ближайшие к главной), присвоить значения, равные полусумме этих
# симметричных значений (элементы главной диагонали имеют индексы от [0,0] до [N,N]).

import numpy as np
import random

N = random.randint(2, 5)
print("N =", str(N))
A = np.random.randint(-50, 50, (N, N))
print(str(A) + "\n")

for i in range(1, N-1):
    b = (A[i+1, i-1] + A[i-1, i+1])/2
    A[i+1, i-1] = b
    A[i-1, i+1] = b
print(A)