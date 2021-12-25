dict_1 = [input()]
dict_2 = [input()]
code = [input()]
uncode = [input()]
result_dict_1 = []
result_dict_2 = []
result_code = []
result_uncode = []
par = {}


for x in dict_1:
    for y in list(x):
        result_dict_1.append(y)

for x in dict_2:
    for y in list(x):
        result_dict_2.append(y)

for x in code:
    for y in list(x):
        result_code.append(y)

for x in uncode:
    for y in list(x):
        result_uncode.append(y)


#Создаем словарь
for i in result_dict_1:
    t = result_dict_1.index(i)
    par[i] = result_dict_2[t]

#Шифрование
for i in result_code:
    if i in par.keys():
        print(par[i], end ='')
print('')

#Дешифрование
inv_par = {value: key for key, value in par.items()}  # Инвертируем словарь
for i in result_uncode:
    if i in inv_par.keys():
        print(inv_par[i], end ='')
