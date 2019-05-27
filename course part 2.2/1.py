import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)
print(N, M)
A = np.random.randint(0, 100, (N, M))
print(A)
mx = 0
indmx = 0
for i in range(M):
    if np.sum(A[:, i]) > mx:
        mx = np.sum(A[:, i])
        indmx = i
print("Столбец с максимальной суммой элементов - " + str(A[:, indmx]))
print("Сумма этого столбца - " + str(mx) + ", " + "номер этого столбца - " + str(indmx + 1))
stmax = 0
for b in A[:, indmx]:
    if b > stmax:
        stmax = b
print("Максимальный элемент этого столбца - " + str(stmax))
