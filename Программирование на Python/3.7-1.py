n = int(input())
lst = []
comand = []

#кладем вводные данные в список,
# получаем двумерный список
cnt_inp = 0
while cnt_inp < n:
    lst1 = [i for i in input().split(';')]
    lst.append(lst1)
    cnt_inp += 1

#Получаем названия команд в отдельный список без повторений
i = 0
for j in lst:
    if [lst[i][0]] in comand:
        i += 1
        continue
    else:
        comand.append([lst[i][0]])
        i += 1
i = 0
for j in lst:
    if [lst[i][2]] in comand:
        i += 1
        continue
    else:
        comand.append([lst[i][2]])
        i += 1

#Готовим сетку для заполнения
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
i = 0
for j in comand:
    for k in range(5):
        comand[i].append(0)
    i += 1

#Проверяем кто победил
i = 0
for j in lst:
    if int(lst[i][1]) > int(lst[i][3]): #первая команда победила
        for k in comand:
            if lst[i][0] in k:
                ind = comand.index(k)
                comand[ind][2] += 1  #увеличиваем количество побед
                comand[ind][1] += 1  #увеличиваем Всего_игр
                comand[ind][5] += 3  #Начисляем за победу
        for k in comand:
            if lst[i][2] in k:
                ind = comand.index(k)
                comand[ind][4] += 1  #Записываем поражение
                comand[ind][1] += 1  # увеличиваем Всего_игр
    elif int(lst[i][1]) < int(lst[i][3]): #вторая команда победила
        for k in comand:
            if lst[i][2] in k:
                ind = comand.index(k)
                comand[ind][2] += 1  # увеличиваем количество побед
                comand[ind][1] += 1  # увеличиваем Всего_игр
                comand[ind][5] += 3  # Начисляем за победу
        for k in comand:
            if lst[i][0] in k:
                ind = comand.index(k)
                comand[ind][4] += 1  #Записываем поражение
                comand[ind][1] += 1  # увеличиваем Всего_игр
    elif int(lst[i][1]) == int(lst[i][3]):  #ничья
        for k in comand:
            if lst[i][0] in k:
                ind = comand.index(k)
                comand[ind][3] += 1  # увеличиваем количество ничьих
                comand[ind][1] += 1  # увеличиваем Всего_игр
                comand[ind][5] += 1  # Начисляем за ничью
            if lst[i][2] in k:
                ind = comand.index(k)
                comand[ind][3] += 1  # увеличиваем количество ничьих
                comand[ind][1] += 1  # увеличиваем Всего_игр
                comand[ind][5] += 1  # Начисляем за ничью
    i += 1

#Выводим
for j in comand:
    ind = comand.index(j)
    print(str(comand[ind][0]) + ':' + str(comand[ind][1]) + ' ' + str(comand[ind][2])
          + ' ' + str(comand[ind][3]) + ' ' + str(comand[ind][4]) + ' '+ str(comand[ind][5]))
    