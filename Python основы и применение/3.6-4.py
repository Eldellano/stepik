from xml.etree import ElementTree


color = {'red': 0, 'green': 0, 'blue': 0}
level = 1
tree = ElementTree.fromstring(input())
root = tree.items()
for value in tree.attrib.values():
    color[value] += level


def count_color(i, level):
    branch = i.attrib
    for value in branch.values():
        level += 1
        color[value] += level
    for j in i:
        count_color(j, level)


for i in tree:
    count_color(i, level)

for value in color.values():
    print(value, end=' ')
