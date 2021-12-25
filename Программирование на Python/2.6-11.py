n = int(input())
cnt_char = 1  #Счетчик чисел для заполнения
start_range = 0
stop = n ** 2
cnt_itter = 1

#Генерируем новую матрицу
lst = [[0] * n for i in range(n)]

#Заполняем и заворачиваем матрицу
while cnt_char <= stop:
    n -= start_range
    if start_range > 1:  #увеличиваем n для иттераций
         n += cnt_itter
         cnt_itter += 1
    for i in range(start_range, n):
        lst[start_range][i] = cnt_char
        cnt_char += 1
    for i in range(start_range + 1, n):
        lst[i][n - 1] = cnt_char
        cnt_char += 1
    for i in reversed(range(start_range, n - 1)):
        lst[n - 1][i] = cnt_char
        cnt_char += 1
    for i in reversed(range(start_range + 1, n - 1)):
        lst[i][start_range] = cnt_char
        cnt_char += 1
    if start_range == stop:
        break
    start_range += 1

#Вывод итоговой матрицы
for i in lst:
    print('')
    for j in i:
        print(j, end=' ')
