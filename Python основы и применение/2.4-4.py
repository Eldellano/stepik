lst = []
with open ('dataset_24465_4.txt', 'r') as file, open ('outfile.txt', 'w') as out_file:
    for line in file:
        lst.append(line.strip())
    lst.reverse()
    content = '\n'.join(lst)
    out_file.write(content)
