def select(arr, dim):
    alg_count = [0, 0]
    for k in range(0, dim - 1):  # -1, т.к. последний элемент обменивать уже не надо
        m = k  # в m хранится минимальное значение
        i = k + 1  # откуда начинать поиск минимума (элемент следующий за k)
        for i in range(i, dim):
            alg_count[0] += 1
            if arr[i] < arr[m]:
                m = i
        if k != m:
            t = arr[k]
            arr[k] = arr[m]
            arr[m] = t
            alg_count[1] += 1
    return alg_count
