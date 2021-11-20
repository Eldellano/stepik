n = int(input())  # число строк
dictionary = {}  # классы и потомки
queue_descr = []  # проверка
for i in range(1, n + 1):
    a, *b = input().replace(":", " ").split()
    dictionary[a] = b
q = int(input())  # число запросов
for i in range(1, q + 1):
    queue_descr.append(input().split())


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not dictionary.get(start):
        return None
    for i in dictionary[start]:
        if i not in path:
            newpath = find_all_paths(dictionary, i, end, path)
            if newpath:
                return newpath
    return None


def class_check():  # проверяем соответвие классов
    for i in queue_descr:
        parent = i[0]
        child = i[1]
        if parent == child:
            print('Yes')
        elif find_all_paths(dictionary, child, parent):
            print('Yes')

        else:
            print('No')


class_check()