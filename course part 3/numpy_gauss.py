import numpy as np  # импортируем библиотеку

input_path = "input/"
my_variant = "12"
file_name = input_path + "gauss_" + my_variant + "_"

file = open('nympy-gauss-slv.csv', 'wb+')
file.truncate()
for i in range(1, 6):
    task_file = file_name + str(i) + ".csv"
    print("\n\nЧитаем: ", task_file)

    # --- исходные данные читаем из файла task_file
    m = np.genfromtxt(task_file, delimiter=';')
    myA = np.genfromtxt(task_file, delimiter=';', usecols=(range(len(m-1))))
    myB = np.genfromtxt(task_file, delimiter=';', usecols=(len(m)))
    # --- end of исходные данные

    print("Задача " + str(i))
    print("Матрица A:")
    print(myA)
    print("Вектор правых частей B:")
    print(myB)

    slv = np.linalg.solve(myA, myB)

    print("Решение задачи " + str(i) + " ", slv)
    np.savetxt(file, np.array([slv]), delimiter=',')
file.close()
