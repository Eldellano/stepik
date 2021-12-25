c = 0
d = 0
while True:
    a = int(input())
    b = a ** 2
    c += b
    d += a
    if d == 0:
        break
print(c)
