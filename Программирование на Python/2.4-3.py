a = input()
a = a.upper()
cnt = len(a) #кол-во символов

cnt_c = a.count('C')
cnt_g = a.count('G')
percent = ((cnt_c + cnt_g) / cnt) * 100

print(percent)
