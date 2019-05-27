# имя проекта:numpy-example
# номер версии:1.0
# имя файла:example_3.py
# автор и его учебная группа:И. Поселеннов, ЭУ-142
# дата создания:20.03.2019
# дата последней модификации:25.03.2019
# связанные файлы:пакеты numpy,matplotlib
# описание:линейная алгебра
# версия Python:3.6

import numpy as np

import numpy.matlib
import numpy.linalg

m1 = np.arange(1, 10).reshape(3, 3)
print(m1)

m2 = np.identity(3)
print(m2)
# Транспонируем первую матрицу, а также посчитаем след и детерминант второй:

m1.transpose()
print(m1)

m2.trace()
print(m2)

det = np.linalg.det(m2)
print(det)

# Матрицы можно складывать, умножать на число, умножать на вектор, а также умножать на другую матрицу:

print(m1+m2)

print(m1*3)

m1 + np.array([1,2,3])
print(m1*m2)

# Посчитать матрицу, обратную к данной, можно функцией np.linalg.inv:
m3 = np.matlib.rand(3, 3)
(m3 * np.linalg.inv(m3))
print(m3)

print((m3 * np.linalg.inv(m3)).round())
