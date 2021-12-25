n = int(input())
lst = []
lst_1 = []
new_lst_1 = []

for i in range(n):
    word = input()
    lst.append(word.lower())

l = int(input())
for i in range(l):
    string = input().split(' ')
    lst_1.append(string)

#Перебираем двумерный список в одномерный
for i in lst_1:
    for j in i:
        n = str(j.lower())
        new_lst_1.append(n)

cnt = 0
for i in set(new_lst_1):
    if i not in lst:
        print(i)
    