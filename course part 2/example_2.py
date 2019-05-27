# имя проекта: numpy-example
# номер версии: 1.0
# имя файла: example_2.py
# автор и его учебная группа: Е. Волков, ЭУ-142
# дата создания: 20.03.2019
# дата последней модификации: 25.03.2019
# связанные файлы: пакеты numpy, matplotlib
# описание: простейшие статистические вычисления
# версия Python: 3.6
import numpy as np
import matplotlib.pyplot as plt

ones = np.ones(50)
rnd = np.random.random(50) * 0.1
samples = ones + rnd
# Посчитаем среднее:
np.average(samples)
np.mean(samples)
# Медиану:
np.median(samples)
# Процентили:
np.percentile(samples, 50)
np.percentile(samples, 95)
np.percentile(samples, 99)
# Максимум, минимум, peak-to-peak:
samples.max()
samples.min()
samples.ptp()
# А заодно уж и стандартное отклонение с дисперсией:
np.std(samples)
np.var(samples)
# Использованная выше функция np.random.random генерирует случайные числа с равномерным распределением.
# А если мы хотели бы использовать нормальноераспределение? Нет проблем:

samples = np.random.normal(loc=0, scale=5, size=100000)
plt.hist(samples, 200)
plt.show()
