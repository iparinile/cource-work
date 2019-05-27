import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)
print(N, M)
A = np.random.randint(0, 100, (N, M))
print(str(A) + "\n")

M_sr = np.mean(A, axis=0)
N_sr = np.mean(A, axis=1)

N_sr = np.append(N_sr, None)

A = np.vstack((A, M_sr))
A = np.hstack((A, N_sr.reshape(-1, 1)))

print(A)
