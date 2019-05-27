def insert(arr, dim):
    alg_count = [0, 0]  # массив для показателей эффективности

    for i in range(1, dim):  # Основной цикл со 2-го элемента право
        temp = arr[i]  # Запомним элемент для сравнения
        j = i - 1
        while j >= 0:  # Ищем влево ближайший меньший
            alg_count[0] += 1  # Считаем операции сравнения
            if arr[j] > temp:
                alg_count[1] += 1  # Считаем операции перестановки
                arr[j + 1] = arr[j]  # Сдвигаем элемент влево, а на его место ставим наименьший
                arr[j] = temp
            j -= 1
    print(alg_count)
import random
arry = [random.randint(0, 20) for i in range(20)]
print(arry)
insert(arry, len(arry))
print(arry)