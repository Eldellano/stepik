a = int(input())
b = int(input())
c = int(input())
d = int(input())

res = 0

# Выводим горизонтальную строку (Шапку)
horizon = range(c, d + 1)
max_index = len(horizon) - 1
cnt = 0

while cnt <= max_index:
    num = horizon[cnt]
    print('\t' + str(num), end='')
    cnt += 1

vert = range(a, b + 1)

cnt_1 = len(horizon)  # Считаем длину списков
cnt_2 = len(vert)
cnt_3 = 0

n = 0

for i in range(a, b + 1):
    print()
    print(str(vert[n]) + '\t', end='')
    n += 1
    for j in range(c, d + 1):
        cnt_3 += 1
        res = j * i

        print(str(res) + '\t', end='')
