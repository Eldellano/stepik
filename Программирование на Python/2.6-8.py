n = int(input())
a = []
b = []
num = 1
cnt = 1
dl = 0
final_cnt = 0
final_cnt2 = 0

while dl <= n:
    a.append((str(num) + '') * num)
    dl = len(a)
    num += 1
    cnt += 1

#a = [''.join(a)]

e = ' '
result_list = []
for x in a:
    for y in list(x):
        result_list.append(y)


for i in result_list:
    z = int(i) + 10

    if 76 > final_cnt2 >= 65:
        if z == 11:
            print(11, end = ' ')
            final_cnt2 += 1
            continue

    if final_cnt2 >= 45:
        if z == 11:
            #print(z, end = ' ')
            final_cnt2 += 1
            continue
        print(z, end = ' ')


    if final_cnt2 >= 45 and z == 11:
        print(z, end = ' ')
    elif final_cnt2 < 45:
        print(i, end = ' ')
    final_cnt += 1
    final_cnt2 +=1
    if final_cnt >= n:
        break
print()
