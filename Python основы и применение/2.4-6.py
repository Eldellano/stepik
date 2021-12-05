import os.path


path_lst = []
for current_dir, dirs, files in os.walk('.'):
    for i in files:
        if i.endswith('.py') and current_dir != '.':
            path_lst.append(current_dir.replace('.\\', '').replace('\\', '/'))
            break

path_lst.sort()
with open('outfile.txt', 'w') as out_file:
    content = '\n'.join(path_lst)
    out_file.write(content)
