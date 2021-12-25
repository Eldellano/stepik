a = [int(i) for i in input().split()]
b =[]  # Новый список
cnt = len(a)
n = 0
s = 0  # Итоговое число

for i in a:
    if cnt == 1:  # Если в списке 1 элемент
        b += a
    elif a[0] and n == 0:  # Первый элемент
        s = a[1] + a[-1]
        #print(s)
        n += 1
        b += [s]

    elif n != (cnt - 1):  # a[n] and n != (cnt - 1):
        s = a[n - 1] + a[n + 1]
        n += 1
        b += [s]

    elif a[-1] == 0:  # Если последний элемент 0
        s = a[n - 1] + a[0]
        b += [s]

    elif a[-1]:  # Последний элемент
        s = a[-2] + a[0]
        #n += 1
        b += [s]

for i in b: print(i, end =' ')
