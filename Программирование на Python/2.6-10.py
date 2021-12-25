lst = []
new_lst = []
ind_colums = 0
ind_string = 0

while True:
    result = [(i) for i in input().split()]
    if 'end' in result:
         break
    lst = [int(item) for item in result]
    new_lst.append(result)
lst.clear()

#Генерируем новую матрицу
string = len(new_lst) #Количество строк
columns = len(new_lst[0]) #Количество столбцов
lst = [[0] * columns for i in range(string)]

for i in new_lst:
    #ind_colums = new_lst.index(i)
    border_colums = len(new_lst) #Длина списка для верхней границы
    if ind_colums >= border_colums:
        ind_colums = 0
        continue
    for j in i:
        border_string = len(i)  # Длина списка для верхней границы
        if ind_string >= border_string:
            ind_string = 0
            continue
        lst[ind_colums][ind_string] = (int(new_lst[ind_colums][ind_string - 1]) +
                                       int(new_lst[ind_colums][ind_string - border_string + 1]) +
                                       int(new_lst[ind_colums - 1][ind_string]) +
                                       int(new_lst[ind_colums - border_colums + 1][ind_string]))
        ind_string += 1
    ind_string = 0
    ind_colums += 1
#Вывод итоговой матрицы
for i in lst:
    print('')
    for j in i:
        print(j, end=' ')
        