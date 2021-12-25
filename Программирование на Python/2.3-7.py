a = int(input())
b = int(input())

sm = 0
s = 0
for i in range(a, b+1):
    if i % 3 == 0:
        #sm += a
        s += i
        sm += 1 #Считаем количество делящихся чисел

sr = s / sm
print(sr)