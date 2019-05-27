def select(arry):
    alg_count = [0, 0]  # массив для показателей эффективности
    for i in range(len(arry) - 1):
        m = i
        j = i + 1
        while j < len(arry):
            alg_count[0] += 1
            if arry[j] < arry[m]:
                m = j
            j = j + 1
        arry[i], arry[m] = arry[m], arry[i]
        alg_count[1] += 1
    print(alg_count)
import random
arry = [random.randint(0, 20) for i in range(20)]
print(arry)
select(arry)
print(arry)