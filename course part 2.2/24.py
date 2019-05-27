# Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Дан номер строки L и номер столбца K, при
# помощи которых исходная матрица разбивается на четыре части. Найти
#  сумму элементов каждой части.

import numpy as np
import random

N = random.randint(5, 8)
M = random.randint(5, 8)
print("N =", str(N), " - ", "M =", str(M))
A = np.random.randint(-50, 50, (N, M))
print(str(A) + "\n")

L = random.randint(2, N-2)
K = random.randint(2, M-2)
print("L =", str(L+1), "K =", str(K+1))
M_n = [A[:L, :K], A[:L, K:], A[L:, :K], A[L:, K:]]
for i in range(len(M_n)):
    print(M_n[i], "Сумма элементов =", str(np.sum(M_n[i])), "\n")
