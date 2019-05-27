import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)
print(N, M)
A = np.random.randint(0, 100, (N, M))
print(A)

srmin = np.average(A[0, :])  # Минимальное среднее значение строки
indstr = 0  # Индекс строки с мин. значением
for i in range(N):
    if np.average(A[i, :]) < srmin:
        srmin = np.average(A[i, :])
        indstr = i
print("Строка с наименьшим средним значением - " + str(A[indstr, :]))
print("Наименьшее среднее значение - " + str(srmin))
