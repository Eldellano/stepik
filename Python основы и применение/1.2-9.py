new_list = []
cnt = 0
for obj in objects: # доступная переменная objects
    if obj not in new_list:
        new_list.append(obj)
print(len(new_list))