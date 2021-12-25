lst = [int(i) for i in input().split()]
x = int(input())
dl = len(lst)
poz = -1
count = 0

while count <= dl:
    poz += 1
    count += 1
    if poz >= len(lst):
        break
    if x == lst[poz]:
        print(poz, end=' ')

if x not in lst:
        print('Отсутствует')
        