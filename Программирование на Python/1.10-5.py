a = int(input()) #Необходимо спать не менее
b = int(input()) #Необходимо спать не более
c = int(input()) #Спит
if a <= c <= b:
    print('Это нормально')
elif a > c:
    print('Недосып')
elif b < c:
    print('Пересып')
    