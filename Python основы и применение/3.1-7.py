a = input()
b = input()

start = 0
cnt = 0

for i in range(len(a)):
    if a.startswith(b, start):
        cnt += 1
        start += 1
    else:
        start += 1
print(cnt)
