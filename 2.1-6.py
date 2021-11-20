n = int(input())  # число строк
dictionary = {}  # классы и потомки
queue_descr = []  # проверка
exc_lst = []  # Хранение исключений
for i in range(1, n + 1):
    a, *b = input().replace(":", " ").split()
    dictionary[a] = b
q = int(input())  # число запросов
for i in range(1, q + 1):
    queue_descr.append(input())


def find_all_paths(dictionary, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not dictionary.get(start):
        return []
    for i in dictionary[start]:
        if i not in path:
            newpath = find_all_paths(dictionary, i, end, path)
            if newpath:
                return newpath
    return []


def class_check():  # проверяем соответвие классов
    for parent in queue_descr:
        for child in exc_lst:
            if find_all_paths(dictionary, parent, child):
                print(parent)
                break
        exc_lst.append(parent)


class_check()#
