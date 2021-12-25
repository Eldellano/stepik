def modify_list(l):
    new_list = []
    for i in reversed(l):
        if i % 2 != 0:
            l.remove(i)
    for i in l:
        i = i // 2
        new_list.append(i)
    l.clear()
    l.extend(new_list)
    