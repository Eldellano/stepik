import simplecrypt


password = []

with open('encrypted.bin', 'rb') as inp:
    encrypted = inp.read()

inf = open('passwords.txt', 'r')
for i in inf.readlines():
    password.append(i.strip())
inf.close()


def decription():
    cnt = 0
    for i in range(len(password)):
        print(cnt, i)  # Для визуализации процесса перебора
        try:
            print(simplecrypt.decrypt(password[cnt], encrypted).decode('utf8'))
            cnt += 1
        except:
            cnt += 1


decription()
