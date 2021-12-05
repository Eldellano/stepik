# import itertools
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

# print(list(itertools.takewhile(lambda x: x <= 31, primes())))




