import json
from collections import Counter

json_in = input().strip()
dump = json.loads(json_in)
class_names = []
class_parent = []
out_lst = []
graph = {}
all_classes = []
for i in dump:
    child = i['name']
    parent = i['parents']
    graph[child] = set(parent)
for i in dump:
    class_names.append(i['name'])
    class_parent.append(i['parents'])

for i in class_names:
    if i not in all_classes:
        all_classes.append(i)
for i in class_parent:
    for j in i:
        if j not in all_classes:
            all_classes.append(j)

stack = []
def class_count(graph, start):  # via: https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for i in graph[vertex]:
                if i not in visited:
                    stack.append(i)
            stack.extend(graph[vertex] - visited)
    for i in visited:
        out_lst.append(i)


def class_check():
    for i in all_classes:
        child = i
        class_count(graph, child)


class_check()
d = dict(Counter(out_lst))
sorted_dict = dict(sorted(d.items(), key=lambda x: x[0]))
for key, value in sorted_dict.items():
    print(f'{key} : {value}')
