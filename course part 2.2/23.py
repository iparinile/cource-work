# Создать квадратную матрицу A, имеющую N строк и N столбцов со
# случайными элементами. Найти сумму элементов, расположенных выше
# главной диагонали, и произведение элементов, расположенных выше
# побочной диагонали (элементы главной диагонали имеют индексы от [0,0]
# до [N,N], а элементы побочной диагонали — от [N,0] до [0,N]).

import numpy as np
import random

N = random.randint(2, 5)
print("N =", str(N))
A = np.random.randint(-50, 50, (N, N))
print(str(A) + "\n")

R_sum = []
for i in range(1, N):
    a = (np.diagonal(A, i).tolist())
    for k in a:
        R_sum.append(k)
print("Элементы выше главной диагонали -", str(R_sum))
print("Сумма элементов выше главное диагонали =", str(np.sum(R_sum)), "\n")

R_pr = []
A = A[::-1]  # Отражение матрицы
for i in range(-1, -N, -1):
    a = (np.diagonal(A, i).tolist())
    for k in a:
        R_pr.append(k)
print("Элементы выше побочной диагонали -", str(R_pr))
print("Произведение элементов выше побочной диагонали =", str(np.prod(R_pr)))
