import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)
print(N, M)
A = np.random.randint(0, 100, (N, M))
print(A)

srmax = 0  # Максимальное среднее значение строки
indstr = 0  # Индекс строки с макс. значением
for i in range(N):
    if np.average(A[i, :]) > srmax:
        srmax = np.average(A[i, :])
        indstr = i
print("Строка с наибольшим средним значением - " + str(A[indstr, :]))
print("Наибольшее среднее значение - " + str(srmax))
