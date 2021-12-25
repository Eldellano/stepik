a = [int(i) for i in input().split()]
b = []
n = 0
dl = len(a) - 1
for i in a:
    cnt = a.count(a[n])
    if i in b:  # Проверяем есть ли элемент в новом списке b
        n += 1
        continue
    elif cnt >= 2:
        b.append(i)
        n += 1
    elif cnt == 1:
        n += 1
    cnt = 0
for i in b: print(i, end =' ')
