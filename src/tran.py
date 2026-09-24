#Программа Транспонирование (вариант1)
n = 0
m = 0
run = True
print("*Количество строк должно быть целым числом, в противном случае значение будет округлено")

while (run):
    #Ввод
    while n < 1:
        n = input('Введите количество строк (n): ')
        try:
            n = float(n)
        except:
            print("Недопустимый ввод строк, повторите попытку")
            n = 0
            continue
        else:
            n = round(n)
            if n < 1:
                print('Ввод должен быть больше 0!')

    while m < 1:
        m = input('Введите количество столбцов (m): ')
        try:
            m = float(m)
        except:
            print("Недопустимый ввод строк, повторите попытку")
            m = 0
            continue
        else:
            m = round(m)
            if m < 1:
                 print('Ввод должен быть больше 0!')


    #Создание матрицы
    matrix = []
    for i in range(n):
        matrix.append(list())
        for j in range(m):
            matrix[i].append(0)

    crct = True
    #Заполнение матрицы построчно
    for i in range(n):
        print(f'Введите числа для {i+1}-й строки:')
        for j in range(m):
           while(crct):
               matrix[i][j] = input()
               try:
                   matrix[i][j] = float(matrix[i][j])
               except:
                   matrix[i][j] = input("Ввод должен быть вещественным числом, повторите попытку")
               else:
                   break
    print("Успешный ввод матрицы")



    #Вывод
    print(f'\nМатрица {m}х{n}:')
    for i in range(m):
        for j in range(n):
            if (j == n-1):
                print(matrix[j][i])
            else:
                print(matrix[j][i], end = " ")
    

    #Запрос на повторный запуск
    answ = ""
    while (answ != 'Д' and answ != 'д' and answ != 'Н' and answ != 'н'):
        answ = input("Повторить запуск?\n[Д] - да, [Н] - нет: ")
        if (answ == 'Н' or answ == 'н'):
            run = False
        elif (answ == 'Д' or answ == 'д'):
            run = True
            n = 0
            m = 0
        else:
            print("Такого варианта ответа нет, повторите ввод")