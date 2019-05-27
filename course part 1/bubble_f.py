def bubble(arr, dim):
    alg_count = [0, 0]  # Массив для показателей эффективности
    for i in range(dim - 1):  # Основной цикл для всех элементов
        for j in range(dim - i - 1):  # Цикл для оставшейся части меньших элементов
            alg_count[0] += 1
            if arr[j] > arr[j + 1]:  # Сравниваем элементы
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Меняем элементы местами
                alg_count[1] += 1
    return alg_count
