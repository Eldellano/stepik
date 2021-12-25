a = int(input())  # Вводим год

if ((a % 4 == 0) and (a % 100 != 0)):
    print('Високосный')
elif (a % 400 == 0):
    print('Високосный')
else:
    print('Обычный')
