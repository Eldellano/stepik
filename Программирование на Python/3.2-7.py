# Считайте, что функция f(x) уже определена выше. Определять её отдельно не требуется.
n = int(input())
cnt = 0
lst = []
lst_out = {}
while cnt < n:
    item = input()
    lst.append(item)
    cnt +=1

for x in lst:
    x = int(x)
    key = x
    if key in lst_out:
        lst_out[key*10] = lst_out.get(key)
        print(lst_out.get(key))
        continue
    else:
        out = f(x)
        lst_out[key] = out
        print(lst_out.get(key))
        