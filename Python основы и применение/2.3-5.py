def primes():
    i = 2
    while True:
        if simple_num(i) is not None:
            out = i
            i += 1
            yield out
        else:
            i += 1


def simple_num(n):
    cnt = 0
    for i in range(2, n // 2 + 1):
        if (n % i == 0):
            cnt += 1
    if (cnt <= 0):
        return n

#Для тестирования
yo = primes()
for i in range(31):
    print(next(yo))

"""
В Pycharm код выполняется не правильно, при yo = primes() for i in range(31): print(next(yo)) выводит числа до 127, 
пытаясь найти ошибку запустил код в pythontutor, и там вывод был как и положено до 31 числа. Отправил решение на степик, 
и оно было принято. В чем проблема неверного поведения кода при запуске в Pycharm я так и не могу понять. 
Напишите пожалуйста, если понимаете что здесь не так. 
"""




