lst = [str(i) for i in input().split()]
lst = [item.lower() for item in lst]
slov = {}

for i in reversed(lst):
    b = lst.count(i)
    key = i
    slov[key] = b

for key,value in slov.items():
    print(key,value)
