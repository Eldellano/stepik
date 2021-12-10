s = input()
a = input()
b = input()
cnt = 0

while True:
    if cnt == 1000:
        print('Impossible')
        break
    elif s.find(a) != -1:
        tmp = s.replace(a, b)
        s = tmp
        cnt += 1
    else:
        print(cnt)
        break
